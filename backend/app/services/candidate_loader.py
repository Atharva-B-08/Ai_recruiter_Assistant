import json
from pathlib import Path

from app.models.candidate import CandidateProfile


DEFAULT_DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _read_json(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def _load_single(file_path: Path):
    data = _read_json(file_path)

    if isinstance(data, list):
        if len(data) != 1:
            raise ValueError(
                f"Expected exactly one record in {file_path.name}, "
                f"but found {len(data)}."
            )

        return data[0]

    if isinstance(data, dict):
        return data

    raise ValueError(
        f"Invalid data format in {file_path.name}. "
        "Expected an object or a list containing one object."
    )


def _load_list(file_path: Path):
    data = _read_json(file_path)

    if not isinstance(data, list):
        raise ValueError(
            f"Expected a list in {file_path.name}."
        )

    return data


def _load_projects(projects_dir: Path):
    if not projects_dir.exists():
        raise FileNotFoundError(
            f"Projects directory not found: {projects_dir}"
        )

    projects = []

    for file_path in sorted(projects_dir.glob("*.json")):
        data = _read_json(file_path)

        if isinstance(data, list):
            projects.extend(data)

        elif isinstance(data, dict):
            projects.append(data)

        else:
            raise ValueError(
                f"Invalid project data format in {file_path.name}."
            )

    return projects


def load_candidate(data_dir: Path | str | None = None) -> CandidateProfile:
    """
    Load all candidate JSON files and return
    one validated CandidateProfile object.
    """

    data_path = Path(data_dir) if data_dir else DEFAULT_DATA_DIR

    candidate = CandidateProfile(
        profile=_load_single(data_path / "profile.json"),

        education=_load_list(
            data_path / "education.json"
        ),

        experience=_load_list(
            data_path / "experience.json"
        ),

        skills=_load_single(
            data_path / "skills.json"
        ),

        achievements=_load_list(
            data_path / "achievements.json"
        ),

        certificates=_load_list(
            data_path / "certificates.json"
        ),

        socials=_load_single(
            data_path / "socials.json"
        ),

        projects=_load_projects(
            data_path / "projects"
        ),
    )

    return candidate