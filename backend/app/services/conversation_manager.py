from app.models.conversation import (
    Conversation,
    ConversationMessage,
)
from uuid import uuid4


class ConversationManager:
    def __init__(self):
        self.conversations: dict[str, Conversation] = {}

    def create_conversation_id(self) -> str:
        return str(uuid4())

    def create_conversation(
        self,
        conversation_id: str,
    ) -> Conversation:
        conversation = Conversation(
            conversation_id=conversation_id
        )

        self.conversations[conversation_id] = conversation

        return conversation

    def get_conversation(
        self,
        conversation_id: str,
    ) -> Conversation | None:
        return self.conversations.get(conversation_id)

    def add_message(
        self,
        conversation_id: str,
        role: str,
        content: str,
    ) -> Conversation:
        conversation = self.get_conversation(conversation_id)

        if conversation is None:
            conversation = self.create_conversation(
                conversation_id
            )

        conversation.messages.append(
            ConversationMessage(
                role=role,
                content=content,
            )
        )

        return conversation