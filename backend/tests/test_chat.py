from app.models.chat import ChatRequest, ChatResponse


def test_chat_request():
    request = ChatRequest(
        question="Tell me about Atharva's backend skills."
    )

    assert request.question == (
        "Tell me about Atharva's backend skills."
    )


def test_chat_response():
    response = ChatResponse(
        answer="Atharva has experience with Java and Spring Boot."
    )

    assert response.answer == (
        "Atharva has experience with Java and Spring Boot."
    )


def test_chat_request_rejects_empty_question():
    from pydantic import ValidationError

    try:
        ChatRequest(question="")
        assert False
    except ValidationError:
        assert True