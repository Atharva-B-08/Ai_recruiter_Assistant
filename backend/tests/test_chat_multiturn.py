from fastapi.testclient import TestClient

from app.main import app


def test_chat_supports_multiple_messages(monkeypatch):
    answers = []

    class FakeGroqService:
        def generate_answer(
            self,
            question: str,
            candidate_context: str,
            conversation_history=None,
        ) -> str:

            answers.append(
                {
                    "question": question,
                    "history": conversation_history,
                }
            )

            assert "Atharva" in candidate_context

            if question == "Tell me about yourself.":
                return "Atharva is a Computer Engineering graduate."

            if question == "What projects have you worked on?":
                assert conversation_history is not None
                assert len(conversation_history) == 2

                return (
                    "Atharva has worked on FinTrack, "
                    "Smart Contact Manager and SignMate."
                )

            raise AssertionError(
                f"Unexpected question: {question}"
            )

    monkeypatch.setattr(
        "app.api.chat.groq_service",
        FakeGroqService(),
    )

    with TestClient(app) as client:

        # First recruiter question
        first_response = client.post(
            "/chat",
            json={
                "question": "Tell me about yourself."
            },
        )

        assert first_response.status_code == 200

        first_data = first_response.json()

        assert "answer" in first_data
        assert "conversation_id" in first_data

        conversation_id = first_data["conversation_id"]

        assert conversation_id

        # Second recruiter question using the same conversation
        second_response = client.post(
            "/chat",
            json={
                "question": "What projects have you worked on?",
                "conversation_id": conversation_id,
            },
        )

        assert second_response.status_code == 200

        second_data = second_response.json()

        assert "answer" in second_data
        assert "conversation_id" in second_data

        # The conversation ID must remain the same.
        assert (
            second_data["conversation_id"]
            == conversation_id
        )

        assert (
            second_data["answer"]
            == (
                "Atharva has worked on FinTrack, "
                "Smart Contact Manager and SignMate."
            )
        )

    # The first Groq call has no previous conversation.
    assert answers[0]["history"] == []

    # The second Groq call receives the first
    # user question and first assistant answer.
    assert len(answers[1]["history"]) == 2

    assert answers[1]["history"][0].role == "user"
    assert (
        answers[1]["history"][0].content
        == "Tell me about yourself."
    )

    assert answers[1]["history"][1].role == "assistant"
    assert (
        answers[1]["history"][1].content
        == "Atharva is a Computer Engineering graduate."
    )