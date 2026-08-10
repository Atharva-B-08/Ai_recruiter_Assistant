from app.services.candidate_loader import load_candidate
from app.services.context_builder import build_candidate_context


def test_build_candidate_context():
    candidate = load_candidate()

    context = build_candidate_context(candidate)

    assert isinstance(context, str)

    assert "## PROFILE" in context
    assert "## EDUCATION" in context
    assert "## EXPERIENCE" in context
    assert "## SKILLS" in context
    assert "## ACHIEVEMENTS" in context
    assert "## CERTIFICATES" in context
    assert "## SOCIAL LINKS" in context
    assert "## PROJECTS" in context


def test_context_contains_candidate_information():
    candidate = load_candidate()

    context = build_candidate_context(candidate)

    assert "Atharva Butte" in context
    assert "Spring Boot" in context
    assert "Java" in context
    assert "FinTrack" in context
    assert "Smart Contact Manager" in context
    assert "SignMate - Sign Language Interpreter" in context


def test_context_contains_project_information():
    candidate = load_candidate()

    context = build_candidate_context(candidate)

    assert "JWT" in context
    assert "PostgreSQL" in context
    assert "TensorFlow Lite" in context


def test_context_is_not_empty():
    candidate = load_candidate()

    context = build_candidate_context(candidate)

    assert len(context.strip()) > 0