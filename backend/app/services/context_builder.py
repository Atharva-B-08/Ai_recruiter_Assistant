import json

from app.models.candidate import CandidateProfile


def _format_section(title: str, data) -> str:
    """
    Convert a section of candidate data into readable JSON text.
    """

    if hasattr(data, "model_dump"):
        data = data.model_dump(
            mode="json",
            exclude_none=True
        )

    elif isinstance(data, list):
        data = [
            item.model_dump(
                mode="json",
                exclude_none=True
            )
            if hasattr(item, "model_dump")
            else item
            for item in data
        ]

    return (
        f"## {title}\n"
        f"{json.dumps(data, indent=2, ensure_ascii=False)}"
    )


def build_candidate_context(candidate: CandidateProfile) -> str:
    """
    Convert a validated CandidateProfile into a structured,
    AI-ready context string.
    """

    sections = [
        _format_section("PROFILE", candidate.profile),
        _format_section("EDUCATION", candidate.education),
        _format_section("EXPERIENCE", candidate.experience),
        _format_section("SKILLS", candidate.skills),
        _format_section("ACHIEVEMENTS", candidate.achievements),
        _format_section("CERTIFICATES", candidate.certificates),
        _format_section("SOCIAL LINKS", candidate.socials),
        _format_section("PROJECTS", candidate.projects),
    ]
    
    return "\n\n".join(sections)