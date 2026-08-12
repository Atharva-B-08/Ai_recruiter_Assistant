from app.models.chat import ChatRequest, ChatResponse


def test_chat_request():
    request = ChatRequest(
        question="Tell me about Atharva."
    )

    assert request.question == "Tell me about Atharva."
    assert request.conversation_id is None


def test_chat_request_with_conversation_id():
    request = ChatRequest(
        question="What project did you work on?",
        conversation_id="conversation-123",
    )

    assert request.question == "What project did you work on?"
    assert request.conversation_id == "conversation-123"


def test_chat_response():
    response = ChatResponse(
        answer="Atharva has experience with Java and Spring Boot.",
        conversation_id="conversation-123",
    )

    assert response.answer == (
        "Atharva has experience with Java and Spring Boot."
    )
    assert response.conversation_id == "conversation-123"