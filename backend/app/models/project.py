from pydantic import BaseModel, Field


class Technologies(BaseModel):
    backend: list[str] = []
    frontend: list[str] = []
    database: list[str] = []
    authentication: list[str] = []
    machine_learning: list[str] = []
    tools: list[str] = []


class Architecture(BaseModel):
    pattern: str
    layers: list[str] = []


class Database(BaseModel):
    database_name: str
    tables: list[str] = []
    relationships: list[str] = []


class Security(BaseModel):
    authentication: str
    authorization: str
    password_encryption: str


class Project(BaseModel):
    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    type: str = Field(min_length=1)
    role: str = Field(min_length=1)
    duration: str = Field(min_length=1)
    team_size: int = Field(ge=1)
    status: str = Field(min_length=1)

    summary: str = Field(min_length=1)
    problem_statement: str = Field(min_length=1)
    objectives: list[str] = []

    technologies: Technologies
    features: list[str] = []

    architecture: Architecture
    database: Database

    api_modules: list[str] = []
    security: Security

    workflow: list[str] = []
    my_contributions: list[str] = []

    challenges: list[str] = []
    solutions: list[str] = []
    learnings: list[str] = []

    future_improvements: list[str] = []
    skills_demonstrated: list[str] = []

    github: str
    live_demo: str
    images: list[str] = []

    resume_description: str = Field(min_length=1)