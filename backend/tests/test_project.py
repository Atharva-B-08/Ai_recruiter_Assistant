import json
from pathlib import Path

from app.models.project import Project


PROJECTS_DIR = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "projects"
)


def load_project(filename: str) -> Project:
    file_path = PROJECTS_DIR / filename

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return Project(**data[0])


def test_fintrack():
    project = load_project("fintrack.json")

    assert project.id == "fintrack"
    assert project.name == "FinTrack"
    assert project.role == "Full Stack Developer"
    assert project.technologies.backend
    assert "Spring Boot" in project.technologies.backend
    assert project.architecture.pattern == "Layered Architecture"


def test_smart_contact_manager():
    project = load_project("smart-contact-manager.json")

    assert project.id == "smart-contact-manager"
    assert project.name == "Smart Contact Manager"
    assert project.role == "Full Stack Developer"
    assert "Spring Security" in project.technologies.backend
    assert project.database.database_name == "MySQL"


def test_signmate():
    project = load_project("signmate.json")

    assert project.id == "signmate"
    assert project.name == "SignMate - Sign Language Interpreter"
    assert project.role == "Machine Learning Developer"
    assert "Python" in project.technologies.machine_learning
    assert "TensorFlow Lite" in project.technologies.machine_learning
    assert project.database.tables == []