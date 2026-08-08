from pydantic import BaseModel, Field


class Education(BaseModel):
    degree: str = Field(min_length=1)
    branch: str
    college: str = Field(min_length=1)
    university: str = Field(min_length=1)
    cgpa: float | None = None
    percentage: float
    status: str = Field(min_length=1)
    start_year: int
    end_year: int 