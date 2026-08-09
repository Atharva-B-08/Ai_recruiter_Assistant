from pydantic import BaseModel, Field


class Skills(BaseModel):
    languages: list[str]
    backend: list[str]
    frontend: list[str]
    database: list[str]
    messaging_platforms: list[str] 
    tools: list[str]
    cloud: list[str]
    version_control: list[str]
    other: list[str]
