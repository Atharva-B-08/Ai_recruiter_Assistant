from app.services.conversation_manager import ConversationManager


def test_create_conversation():
    manager = ConversationManager()

    conversation = manager.create_conversation(
        "conversation-1"
    )

    assert conversation.conversation_id == "conversation-1"
    assert conversation.messages == []


def test_get_existing_conversation():
    manager = ConversationManager()

    manager.create_conversation("conversation-1")

    conversation = manager.get_conversation(
        "conversation-1"
    )

    assert conversation is not None
    assert conversation.conversation_id == "conversation-1"


def test_get_missing_conversation():
    manager = ConversationManager()

    conversation = manager.get_conversation(
        "does-not-exist"
    )

    assert conversation is None


def test_add_message():
    manager = ConversationManager()

    manager.add_message(
        conversation_id="conversation-1",
        role="user",
        content="Tell me about FinTrack.",
    )

    conversation = manager.get_conversation(
        "conversation-1"
    )

    assert conversation is not None
    assert len(conversation.messages) == 1
    assert conversation.messages[0].role == "user"
    assert (
        conversation.messages[0].content
        == "Tell me about FinTrack."
    )


def test_add_multiple_messages():
    manager = ConversationManager()

    manager.add_message(
        "conversation-1",
        "user",
        "Tell me about FinTrack.",
    )

    manager.add_message(
        "conversation-1",
        "assistant",
        "FinTrack is a personal finance application.",
    )

    conversation = manager.get_conversation(
        "conversation-1"
    )

    assert conversation is not None
    assert len(conversation.messages) == 2

    assert conversation.messages[0].role == "user"
    assert conversation.messages[1].role == "assistant"


def test_conversation_stores_multiple_messages():
    manager = ConversationManager()

    conversation_id = manager.create_conversation_id()

    manager.add_message(
        conversation_id,
        "user",
        "Tell me about your projects.",
    )

    manager.add_message(
        conversation_id,
        "assistant",
        "I have worked on FinTrack, Smart Contact Manager and SignMate.",
    )

    manager.add_message(
        conversation_id,
        "user",
        "What technology did you use for FinTrack?",
    )

    conversation = manager.get_conversation(conversation_id)

    assert conversation is not None
    assert len(conversation.messages) == 3

    assert conversation.messages[0].role == "user"
    assert conversation.messages[0].content == (
        "Tell me about your projects."
    )

    assert conversation.messages[1].role == "assistant"

    assert conversation.messages[2].role == "user"
    assert conversation.messages[2].content == (
        "What technology did you use for FinTrack?"
    )


def test_conversations_are_independent():
    manager = ConversationManager()

    first_id = manager.create_conversation_id()
    second_id = manager.create_conversation_id()

    manager.add_message(
        first_id,
        "user",
        "Tell me about FinTrack.",
    )

    manager.add_message(
        second_id,
        "user",
        "Tell me about SignMate.",
    )

    first_conversation = manager.get_conversation(first_id)
    second_conversation = manager.get_conversation(second_id)

    assert first_conversation is not None
    assert second_conversation is not None

    assert len(first_conversation.messages) == 1
    assert len(second_conversation.messages) == 1

    assert first_conversation.messages[0].content == (
        "Tell me about FinTrack."
    )

    assert second_conversation.messages[0].content == (
        "Tell me about SignMate."
    )