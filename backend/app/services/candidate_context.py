from app.models.candidate import CandidateProfile
from app.services.candidate_loader import load_candidate
from app.services.context_builder import build_candidate_context


class CandidateContextService:
    def __init__(self):
        self.candidate: CandidateProfile | None = None
        self.context: str | None = None

    def load(self) -> None:
        candidate = load_candidate()

        self.candidate = candidate
        self.context = build_candidate_context(candidate)

    def get_candidate(self) -> CandidateProfile:
        if self.candidate is None:
            raise RuntimeError("Candidate data has not been loaded.")

        return self.candidate

    def get_context(self) -> str:
        if self.context is None:
            raise RuntimeError("Candidate context has not been loaded.")

        return self.context