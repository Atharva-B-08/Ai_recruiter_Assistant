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