from fastapi.testclient import TestClient

from app.main import app


def test_candidate_context_loaded_at_startup():
    with TestClient(app):
        service = app.state.candidate_context_service

        candidate = service.get_candidate()
        context = service.get_context()

        assert candidate is not None
        assert context
        assert "Atharva" in context