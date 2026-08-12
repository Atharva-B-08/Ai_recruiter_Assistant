from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from groq import RateLimitError
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

@router.post("/stream")
def chat_stream(
    request: Request,
    chat_request: ChatRequest,
):
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

    conversation_history = list(conversation.messages)

    # conversation_manager.add_message(
    #     conversation_id=conversation_id,
    #     role="user",
    #     content=chat_request.question,
    # )

    def generate():
        complete_answer = []
        yield f"CONVERSATION_ID:{conversation_id}\n"
        try:
            for chunk in groq_service.stream_answer(
                question=chat_request.question,
                candidate_context=candidate_context,
                conversation_history=conversation_history,
            ):
                complete_answer.append(chunk)
                yield chunk

            answer = "".join(complete_answer)

            # Save messages only after successful completion.
            conversation_manager.add_message(
                conversation_id=conversation_id,
                role="user",
                content=chat_request.question,
            )

            conversation_manager.add_message(
                conversation_id=conversation_id,
                role="assistant",
                content=answer,
            )

        except RateLimitError as error:
            print("GROQ RATE LIMIT ERROR:", error)

            yield (
                "\n\nI'm temporarily unavailable because my AI service "
                "has reached its usage limit. Please try again later "
                "or tomorrow."
            )

        except Exception as error:
            print("GROQ GENERAL ERROR:", repr(error))

            yield (
                "\n\nI'm temporarily unable to process your request. "
                "Please try again later."
            )

    return StreamingResponse(
        generate(),
        media_type="text/plain",
    )