from __future__ import annotations

import re

from app.models.candidate import CandidateProfile
from app.models.project import Project
from app.services.context_builder import _format_section


# These are intentionally small, deterministic routing rules. The candidate
# profile is tiny, so a keyword router is faster, cheaper, and easier to test
# than making another LLM call just to decide which context to send.
SECTION_KEYWORDS = {
    "profile": {
        "about", "yourself", "name", "location", "role", "title",
        "position", "career", "interest", "interests", "fit", "best-fit",
        "best fit", "looking", "fresher", "summary", "contacts"
    },
    "skills": {
        "skill", "skills", "technology", "technologies", "tech", "stack",
        "programming", "language", "languages", "framework", "frameworks",
        "backend", "frontend", "database", "cloud", "tool", "tools", "proficiency", "proficient", 
    },
    "education": {
        "education", "study", "studied", "degree", "college", "university",
        "academic background", "qualification", "qualifications", "cgpa", "graduate", "engineering", "bachelor",
    },
    "experience": {
        "experience", "work experience", "employment", "job", "jobs", "role",
        "internship", "internships", "professional experience", "intern",
    },
    "achievements": {
        "achievement", "achievements", "award", "awards", "leetcode", "rank",
        "ranking", "contest", "problem solving", "dsa", "DSA", "competitive programming", "competitive coding", "hackthon", "hackathons", "Problem solved"
    },
    "certificates": {
        "certificate", "certificates", "certification", "certifications",
        "credential", "credentials", "badge" , "course"
    },
    "socials": {
        "contact", "contacts", "email", "phone", "linkedin", "github",
        "social", "socials", "leetcode profile",
    },
}


def _normalize(text: str) -> str:
    text = text.lower().replace("’", "'")
    return re.sub(r"[^a-z0-9+.#\s-]", " ", text)


def _contains(text: str, phrase: str) -> bool:
    phrase = phrase.lower()
    if " " in phrase or "+" in phrase or "." in phrase or "#" in phrase:
        return phrase in text
    return re.search(rf"\b{re.escape(phrase)}\b", text) is not None


def _project_matches(candidate: CandidateProfile, text: str) -> list[Project]:
    matches: list[Project] = []

    for project in candidate.projects:
        names = {
            project.id.lower(),
            project.name.lower(),
            project.name.lower().replace(" - sign language interpreter", ""),
        }

        if any(_contains(text, name) for name in names):
            matches.append(project)

    return matches


def _project_index(candidate: CandidateProfile) -> str:
    """Return a compact project list for broad 'projects' questions."""
    compact_projects = []

    for project in candidate.projects:
        compact_projects.append(
            {
                "name": project.name,
                "type": project.type,
                "role": project.role,
                "duration": project.duration,
                "team_size": project.team_size,
                "status": project.status,
                "summary": project.summary,
                "problem_statement": project.problem_statement,
                "objectives": project.objectives,
                "technologies": project.technologies.model_dump(
                    mode="json", exclude_none=True
                ),
                "features": project.features,
                "github": project.github,
                "live_demo": project.live_demo,
            }
        )

    return _format_section("PROJECTS", compact_projects)


def _full_project_context(project: Project) -> str:
    return _format_section("PROJECT", project)


def get_relevant_candidate_context(
    candidate: CandidateProfile,
    question: str,
    conversation_history=None,
) -> str:
    """
    Select the smallest useful candidate context for a recruiter question.

    The current question and recent conversation history are both considered
    so follow-up questions such as "What technologies did he use?" can still
    resolve to the project mentioned in the previous turn.
    """
    history_text = "\n".join(
        getattr(message, "content", str(message))
        for message in (conversation_history or [])
    )
    current_text = _normalize(question)
    routing_text = _normalize(f"{history_text}\n{question}")

    selected_sections: set[str] = set()
    for section, keywords in SECTION_KEYWORDS.items():
        if any(_contains(current_text, keyword) for keyword in keywords):
            selected_sections.add(section)

    matched_projects = _project_matches(candidate, routing_text)

    # A named project wins over generic section routing. This is important for
    # follow-ups such as "his core features" or "which model did he use?".
    if matched_projects:
        parts = [
            _format_section("PROFILE", candidate.profile),
            *(_full_project_context(project) for project in matched_projects),
        ]
        return "\n\n".join(parts)

    # Asking for projects only needs a compact index, not the full details of
    # all three large project documents.
    if "projects" in current_text or "project" in current_text:
        parts = [
            _format_section("PROFILE", candidate.profile),
            _project_index(candidate),
        ]
        return "\n\n".join(parts)

    # Broad profile questions benefit from a small combination of profile and
    # skills, while avoiding unrelated 5K+ character project documents.
    if not selected_sections:
        selected_sections = {"profile", "skills", "socials"}

    parts: list[str] = []
    section_values = {
        "profile": candidate.profile,
        "education": candidate.education,
        "experience": candidate.experience,
        "skills": candidate.skills,
        "achievements": candidate.achievements,
        "certificates": candidate.certificates,
        "socials": candidate.socials,
    }
    section_titles = {
        "profile": "PROFILE",
        "education": "EDUCATION",
        "experience": "EXPERIENCE",
        "skills": "SKILLS",
        "achievements": "ACHIEVEMENTS",
        "certificates": "CERTIFICATES",
        "socials": "SOCIAL LINKS",
    }

    # Profile is useful context for almost every recruiter-facing answer, but
    # keep it compact by adding it only when another section was selected.
    if selected_sections and "profile" not in selected_sections:
        parts.append(_format_section("PROFILE", candidate.profile))

    for section in (
        "profile",
        "education",
        "experience",
        "skills",
        "achievements",
        "certificates",
        "socials",
    ):
        if section in selected_sections:
            parts.append(_format_section(section_titles[section], section_values[section]))

    return "\n\n".join(parts)
