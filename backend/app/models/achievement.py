from pydantic import BaseModel, Field


class Achievement(BaseModel):
    description: str = Field(min_length=1)