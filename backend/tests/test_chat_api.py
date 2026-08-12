from fastapi.testclient import TestClient

from app.main import app


def test_chat_endpoint(monkeypatch):
    class FakeGroqService:
        def generate_answer(
            self,
            question: str,
            candidate_context: str,
            conversation_history=None,
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

def test_chat_endpoint_with_conversation(monkeypatch):
    answers = []

    class FakeGroqService:
        def generate_answer(
            self,
            question: str,
            candidate_context: str,
            conversation_history=None,
        ) -> str:

            assert "Atharva" in candidate_context

            if question == "Tell me about your projects.":

                assert conversation_history == []

                answer = (
                    "Atharva has worked on FinTrack, "
                    "Smart Contact Manager and SignMate."
                )

            elif question == "Which one uses JWT?":

                assert conversation_history is not None
                assert len(conversation_history) == 2

                assert (
                    conversation_history[0].content
                    == "Tell me about your projects."
                )

                assert (
                    "FinTrack"
                    in conversation_history[1].content
                )

                answer = (
                    "FinTrack uses JWT authentication."
                )

            else:
                raise AssertionError(
                    f"Unexpected question: {question}"
                )

            answers.append(answer)
            return answer

    monkeypatch.setattr(
        "app.api.chat.groq_service",
        FakeGroqService(),
    )

    with TestClient(app) as client:

        # First recruiter question
        first_response = client.post(
            "/chat",
            json={
                "question": "Tell me about your projects."
            },
        )

        assert first_response.status_code == 200

        first_data = first_response.json()

        assert "answer" in first_data
        assert "conversation_id" in first_data

        conversation_id = first_data["conversation_id"]

        assert conversation_id is not None

        # Second recruiter question
        second_response = client.post(
            "/chat",
            json={
                "question": "Which one uses JWT?",
                "conversation_id": conversation_id,
            },
        )

        assert second_response.status_code == 200

        second_data = second_response.json()

        assert "answer" in second_data
        assert "conversation_id" in second_data

        assert (
            second_data["conversation_id"]
            == conversation_id
        )

        assert (
            second_data["answer"]
            == "FinTrack uses JWT authentication."
        )

        assert len(answers) == 2