from fastapi import APIRouter, Request

from app.models.chat import ChatRequest, ChatResponse
from app.services.conversation_manager import ConversationManager
from app.services.groq_service import GroqService


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


groq_service = GroqService()
conversation_manager = ConversationManager()


@router.post("", response_model=ChatResponse)
def chat(
    request: Request,
    chat_request: ChatRequest,
) -> ChatResponse:

    candidate_context_service = (
        request.app.state.candidate_context_service
    )

    candidate_context = (
        candidate_context_service.get_context()
    )

    conversation_id = chat_request.conversation_id

    if conversation_id is None:
        conversation_id = (
            conversation_manager.create_conversation_id()
        )

    conversation = conversation_manager.get_conversation(
        conversation_id
    )

    if conversation is None:
        conversation = conversation_manager.create_conversation(
            conversation_id
        )

    # Keep the history BEFORE adding the current question.
    conversation_history = list(conversation.messages)

    conversation_manager.add_message(
        conversation_id=conversation_id,
        role="user",
        content=chat_request.question,
    )

    answer = groq_service.generate_answer(
        question=chat_request.question,
        candidate_context=candidate_context,
        conversation_history=conversation_history,
    )

    conversation_manager.add_message(
        conversation_id=conversation_id,
        role="assistant",
        content=answer,
    )

    return ChatResponse(
        answer=answer,
        conversation_id=conversation_id,
    )