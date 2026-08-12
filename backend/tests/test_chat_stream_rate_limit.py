from unittest.mock import Mock

from fastapi.testclient import TestClient
from groq import RateLimitError

from app.main import app


def test_chat_stream_handles_rate_limit(monkeypatch):

    class FakeGroqService:
        def stream_answer(
            self,
            question: str,
            candidate_context: str,
            conversation_history=None,
        ):
            response = Mock()
            response.status_code = 429
            response.request = Mock()

            raise RateLimitError(
                "Rate limit reached",
                response=response,
                body={
                    "error": {
                        "message": "Rate limit reached",
                        "type": "tokens",
                        "code": "rate_limit_exceeded",
                    }
                },
            )

            yield

    monkeypatch.setattr(
        "app.api.chat.groq_service",
        FakeGroqService(),
    )

    from app.api.chat import conversation_manager

    conversation_manager.conversations.clear()

    with TestClient(app) as client:
        response = client.post(
            "/chat/stream",
            json={
                "question": "Tell me about FinTrack."
            },
        )

    assert response.status_code == 200

    assert (
        "AI service has reached its usage limit"
        in response.text
    )