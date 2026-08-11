from fastapi import APIRouter, Request

from app.models.chat import ChatRequest, ChatResponse
from app.services.groq_service import GroqService


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


groq_service = GroqService()


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

    answer = groq_service.generate_answer(
        question=chat_request.question,
        candidate_context=candidate_context,
    )

    return ChatResponse(answer=answer)