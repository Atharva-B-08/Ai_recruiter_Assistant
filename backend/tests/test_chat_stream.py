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

    # Conversation event
    assert "event: conversation" in body
    assert "conversation_id" in body

    # Streaming chunks
    assert "event: chunk" in body
    assert "FinTrack " in body
    assert "is a personal finance " in body
    assert "management application." in body

    # Stream completed successfully
    assert "event: done" in body


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

        # First request
        first_response = client.post(
            "/chat/stream",
            json={
                "question": "Tell me about FinTrack."
            },
        )

        assert first_response.status_code == 200

        first_body = first_response.text

        # First response should contain SSE conversation event
        assert "event: conversation" in first_body
        assert "conversation_id" in first_body

        # First response should contain streamed answer
        assert "event: chunk" in first_body
        assert (
            "FinTrack is a personal finance "
            "management application."
        ) in first_body

        # Stream should finish successfully
        assert "event: done" in first_body

        # Extract conversation ID from the first response
        conversation_line = next(
            line
            for line in first_body.splitlines()
            if line.startswith("data: ")
            and "conversation_id" in line
        )

        import json

        conversation_data = json.loads(
            conversation_line.removeprefix("data: ")
        )

        conversation_id = conversation_data["conversation_id"]

        assert conversation_id

        # Second request using the same conversation
        second_response = client.post(
            "/chat/stream",
            json={
                "question": "What technologies did you use?",
                "conversation_id": conversation_id,
            },
        )

        assert second_response.status_code == 200

        second_body = second_response.text

        # Second response should use the same conversation
        assert "event: conversation" in second_body
        assert conversation_id in second_body

        # Second response should contain streamed answer
        assert "event: chunk" in second_body
        assert (
            "I used Java, Spring Boot and React."
        ) in second_body

        # Stream should finish successfully
        assert "event: done" in second_body