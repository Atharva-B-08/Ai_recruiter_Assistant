from unittest.mock import MagicMock

from app.services.groq_service import GroqService


def test_generate_answer():
    fake_response = MagicMock()

    fake_response.choices[0].message.content = (
        "Atharva is a fresher with strong backend development skills "
        "in Java and Spring Boot."
    )

    mock_client = MagicMock()

    mock_client.chat.completions.create.return_value = (
        fake_response
    )

    service = GroqService(client=mock_client)

    answer = service.generate_answer(
        question="Tell me about Atharva's backend skills.",
        candidate_context=(
            "Atharva is a fresher. "
            "Skills include Java and Spring Boot."
        ),
    )

    assert isinstance(answer, str)

    assert "Java" in answer
    assert "Spring Boot" in answer

    mock_client.chat.completions.create.assert_called_once()


def test_generate_answer_returns_string():
    fake_response = MagicMock()

    fake_response.choices[0].message.content = "Test answer"

    mock_client = MagicMock()

    mock_client.chat.completions.create.return_value = (
        fake_response
    )

    service = GroqService(client=mock_client)

    answer = service.generate_answer(
        question="What is the candidate's name?",
        candidate_context="Name: Atharva Butte",
    )

    assert answer == "Test answer"

from types import SimpleNamespace

from app.services.groq_service import GroqService


class FakeCompletions:
    def __init__(self, answer):
        self.answer = answer
        self.last_request = None

    def create(self, **kwargs):
        self.last_request = kwargs

        return SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(
                        content=self.answer
                    )
                )
            ]
        )


class FakeChat:
    def __init__(self, answer):
        self.completions = FakeCompletions(answer)


class FakeGroqClient:
    def __init__(self, answer):
        self.chat = FakeChat(answer)


def test_generate_answer_uses_candidate_context():
    fake_client = FakeGroqClient(
        "Atharva has experience with Java and Spring Boot."
    )

    service = GroqService(client=fake_client)

    context = """
    Name: Atharva Butte
    Skills: Java, Spring Boot
    """

    answer = service.generate_answer(
        question="What backend technologies does Atharva know?",
        candidate_context=context,
    )

    assert "Java" in answer
    assert "Spring Boot" in answer

    request = fake_client.chat.completions.last_request

    assert request is not None
    assert request["temperature"] == 0.2

    user_message = request["messages"][1]["content"]

    assert context in user_message


def test_generate_answer_contains_guardrails():
    fake_client = FakeGroqClient(
        "The requested information is not available."
    )

    service = GroqService(client=fake_client)

    service.generate_answer(
        question="Where did Atharva work professionally?",
        candidate_context="Atharva is a fresher.",
    )

    request = fake_client.chat.completions.last_request

    assert request is not None

    system_message = request["messages"][0]["content"]

    assert "ONLY the candidate information" in system_message
    assert "Never invent" in system_message
    assert "fresher" in system_message
    assert "not available" in system_message


def test_generate_answer_unknown_information():
    fake_client = FakeGroqClient(
        "The information about previous professional employment "
        "is not available."
    )

    service = GroqService(client=fake_client)

    answer = service.generate_answer(
        question="Which company did Atharva work for?",
        candidate_context="Atharva is a fresher.",
    )

    assert "not available" in answer.lower()


def test_generate_answer_handles_empty_response():
    fake_client = FakeGroqClient(None)

    service = GroqService(client=fake_client)

    try:
        service.generate_answer(
            question="Tell me about Atharva.",
            candidate_context="Atharva is a software engineering student.",
        )

        assert False
    except RuntimeError as error:
        assert str(error) == "Groq returned an empty response."


def test_generate_answer_uses_conversation_history():
    class FakeMessage:
        def __init__(self, role, content):
            self.role = role
            self.content = content

    class FakeCompletions:
        def create(self, **kwargs):
            user_prompt = kwargs["messages"][1]["content"]

            assert "Tell me about your projects." in user_prompt
            assert "FinTrack, Smart Contact Manager and SignMate" in user_prompt
            assert "Which one uses JWT?" in user_prompt

            class FakeMessageResponse:
                content = "FinTrack uses JWT authentication."

            class FakeChoice:
                message = FakeMessageResponse()

            class FakeResponse:
                choices = [FakeChoice()]

            return FakeResponse()

    class FakeChat:
        completions = FakeCompletions()

    class FakeClient:
        chat = FakeChat()

    service = GroqService(client=FakeClient())

    history = [
        FakeMessage(
            "user",
            "Tell me about your projects.",
        ),
        FakeMessage(
            "assistant",
            "FinTrack, Smart Contact Manager and SignMate",
        ),
    ]

    answer = service.generate_answer(
        question="Which one uses JWT?",
        candidate_context="FinTrack uses Java, Spring Boot and JWT.",
        conversation_history=history,
    )

    assert answer == "FinTrack uses JWT authentication."