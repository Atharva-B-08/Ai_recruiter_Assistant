from pydantic import BaseModel, Field


class Experience(BaseModel):
    company: str
    position: str = Field(min_length=1)
    duration: str
    description: str = Field(min_length=1)
    Opportunity: str = Field(min_length=1)