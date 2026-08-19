from app.services.candidate_loader import load_candidate
from app.services.context_retriever import get_relevant_candidate_context


def test_named_project_returns_only_that_project():
    candidate = load_candidate()

    context = get_relevant_candidate_context(
        candidate,
        "Tell me about SignMate.",
    )

    assert "## PROJECT" in context
    assert "SignMate - Sign Language Interpreter" in context
    assert "FinTrack" not in context
    assert "Smart Contact Manager" not in context


def test_project_follow_up_uses_conversation_history():
    candidate = load_candidate()

    history = [
        type("Message", (), {"content": "Tell me about SignMate."})(),
        type("Message", (), {"content": "SignMate is an academic project."})(),
    ]

    context = get_relevant_candidate_context(
        candidate,
        "What model did he use?",
        history,
    )

    assert "SignMate - Sign Language Interpreter" in context
    assert "FinTrack" not in context
    assert "Smart Contact Manager" not in context


def test_projects_question_uses_compact_project_index():
    candidate = load_candidate()

    context = get_relevant_candidate_context(
        candidate,
        "What projects has he made?",
    )

    assert "## PROJECTS" in context
    assert "FinTrack" in context
    assert "SignMate - Sign Language Interpreter" in context
    assert "Smart Contact Manager" in context
    assert "## PROJECT\n" not in context


def test_skills_question_does_not_send_full_projects():
    candidate = load_candidate()

    context = get_relevant_candidate_context(
        candidate,
        "What technologies and skills does he know?",
    )

    assert "## SKILLS" in context
    assert "Java" in context
    assert "FinTrack" not in context
    assert "SignMate - Sign Language Interpreter" not in context
    assert "Smart Contact Manager" not in context


def test_contact_question_uses_social_links():
    candidate = load_candidate()

    context = get_relevant_candidate_context(
        candidate,
        "Give me his contact details.",
    )

    assert "## SOCIAL LINKS" in context
    assert "## PROFILE" in context
    assert "FinTrack" not in context
