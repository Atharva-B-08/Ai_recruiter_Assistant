from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(
        min_length=1,
        description="Recruiter's question about the candidate.",
    )
    conversation_id: str | None = Field(
        default=None,
        description="Optional ID used to continue an existing conversation.",
    )


class ChatResponse(BaseModel):
    answer: str
    conversation_id: str