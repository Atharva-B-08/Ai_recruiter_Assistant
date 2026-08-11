from fastapi.testclient import TestClient

from app.main import app


def test_chat_endpoint(monkeypatch):
    class FakeGroqService:
        def generate_answer(
            self,
            question: str,
            candidate_context: str,
        ) -> str:
            assert question == "Tell me about Atharva's skills."
            assert "Atharva" in candidate_context

            return (
                "Atharva has skills in Java, Spring Boot "
                "and backend development."
            )

    monkeypatch.setattr(
        "app.api.chat.groq_service",
        FakeGroqService(),
    )

    with TestClient(app) as client:
        response = client.post(
            "/chat",
            json={
                "question": "Tell me about Atharva's skills."
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert data["answer"] == (
        "Atharva has skills in Java, Spring Boot "
        "and backend development."
    )