import os
import time
from collections import defaultdict, deque
from typing import Deque, DefaultDict

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
import logging


logger = logging.getLogger("uvicorn.error")
_rate_buckets: DefaultDict[str, Deque[float]] = defaultdict(deque)


async def logging_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception:  # noqa: BLE001
        logger.exception("Unhandled error")
        return JSONResponse({"detail": "Internal server error"}, status_code=500)


def add_cors(app):
    allowed = os.getenv("CHAT_ALLOW_ORIGINS", "*")
    origins = [o.strip() for o in allowed.split(",")] if allowed else ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


async def rate_limit_middleware(request: Request, call_next):
    # Simple in-memory sliding window per client IP
    limit = int(os.getenv("RATE_LIMIT_PER_MINUTE", "120"))
    window = 60
    client_ip = request.client.host if request.client else "unknown"
    now = time.time()
    bucket = _rate_buckets[client_ip]
    while bucket and now - bucket[0] > window:
        bucket.popleft()
    if len(bucket) >= limit:
        return JSONResponse({"detail": "Rate limit exceeded"}, status_code=429)
    bucket.append(now)
    return await call_next(request)
