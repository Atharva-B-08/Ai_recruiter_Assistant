from pydantic import BaseModel, Field


class ConversationMessage(BaseModel):
    role: str = Field(min_length=1)
    content: str = Field(min_length=1)


class Conversation(BaseModel):
    conversation_id: str = Field(min_length=1)
    messages: list[ConversationMessage] = Field(default_factory=list)