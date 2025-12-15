# Backend Setup (Floating Docs Chatbot)

1) Install deps  
```bash
pip install -r backend/requirements.txt
```

2) Configure env (.env)  
- QDRANT_URL / QDRANT_API_KEY  
- GEMINI_API_KEY (Gemini via Agents SDK)  

3) Run dev server  
```bash
uvicorn backend.app.main:app --reload
```

4) Health check  
`GET http://localhost:8000/healthz`
