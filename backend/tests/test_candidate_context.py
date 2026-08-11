from unittest.mock import patch

from app.services.candidate_context import CandidateContextService


def test_load_candidate_context():
    service = CandidateContextService()

    with (
        patch(
            "app.services.candidate_context.load_candidate"
        ) as mock_loader,
        patch(
            "app.services.candidate_context.build_candidate_context"
        ) as mock_builder,
    ):
        fake_candidate = object()
        fake_context = "Candidate context"

        mock_loader.return_value = fake_candidate
        mock_builder.return_value = fake_context

        service.load()

        assert service.get_candidate() is fake_candidate
        assert service.get_context() == fake_context

        mock_loader.assert_called_once()
        mock_builder.assert_called_once_with(fake_candidate)


def test_get_candidate_before_loading():
    service = CandidateContextService()

    try:
        service.get_candidate()
        assert False
    except RuntimeError as error:
        assert str(error) == "Candidate data has not been loaded."


def test_get_context_before_loading():
    service = CandidateContextService()

    try:
        service.get_context()
        assert False
    except RuntimeError as error:
        assert str(error) == "Candidate context has not been loaded."