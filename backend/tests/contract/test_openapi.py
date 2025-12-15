import sys
from importlib import util
import pytest

schemathesis_spec = util.find_spec("schemathesis")

@pytest.mark.skipif(schemathesis_spec is None, reason="schemathesis not installed")
def test_openapi_contract():
    import schemathesis
    from backend.app.main import app

    schema = schemathesis.from_asgi("http://localhost:8000/openapi.json", app=app)

    @schema.parametrize()
    def _(case):
        response = case.call_asgi()
        case.validate_response(response)
