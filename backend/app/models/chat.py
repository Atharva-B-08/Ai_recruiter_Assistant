from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(
        min_length=1,
        description="Recruiter's question about the candidate."
    )


class ChatResponse(BaseModel):
    answer: str