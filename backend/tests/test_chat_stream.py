from fastapi.testclient import TestClient

from app.main import app


def test_chat_stream_creates_conversation(monkeypatch):
    class FakeGroqService:
        def stream_answer(
            self,
            question: str,
            candidate_context: str,
            conversation_history=None,
        ):
            assert question == "Tell me about FinTrack."
            assert "Atharva" in candidate_context

            yield "FinTrack "
            yield "is a personal finance "
            yield "management application."

    monkeypatch.setattr(
        "app.api.chat.groq_service",
        FakeGroqService(),
    )

    with TestClient(app) as client:
        response = client.post(
            "/chat/stream",
            json={
                "question": "Tell me about FinTrack."
            },
        )

    assert response.status_code == 200

    body = response.text

    assert "CONVERSATION_ID:" in body
    assert "FinTrack " in body
    assert "is a personal finance " in body
    assert "management application." in body

def test_chat_stream_continues_conversation(monkeypatch):
    call_count = 0

    class FakeGroqService:
        def stream_answer(
            self,
            question: str,
            candidate_context: str,
            conversation_history=None,
        ):
            nonlocal call_count

            call_count += 1

            if call_count == 1:
                assert question == "Tell me about FinTrack."
                assert conversation_history == []

                yield (
                    "FinTrack is a personal finance "
                    "management application."
                )

            else:
                assert question == "What technologies did you use?"
                assert conversation_history is not None
                assert len(conversation_history) == 2

                assert (
                    conversation_history[0].role
                    == "user"
                )

                assert (
                    conversation_history[0].content
                    == "Tell me about FinTrack."
                )

                assert (
                    conversation_history[1].role
                    == "assistant"
                )

                assert (
                    conversation_history[1].content
                    == (
                        "FinTrack is a personal finance "
                        "management application."
                    )
                )

                yield (
                    "I used Java, Spring Boot and React."
                )

    monkeypatch.setattr(
        "app.api.chat.groq_service",
        FakeGroqService(),
    )

    with TestClient(app) as client:
        first_response = client.post(
            "/chat/stream",
            json={
                "question": "Tell me about FinTrack."
            },
        )

        assert first_response.status_code == 200

        first_body = first_response.text

        assert "CONVERSATION_ID:" in first_body

        conversation_id = (
            first_body
            .split("CONVERSATION_ID:", 1)[1]
            .split("\n", 1)[0]
        )

        second_response = client.post(
            "/chat/stream",
            json={
                "question": "What technologies did you use?",
                "conversation_id": conversation_id,
            },
        )

    assert second_response.status_code == 200

    assert (
        "I used Java, Spring Boot and React."
        in second_response.text
    )

    assert call_count == 2