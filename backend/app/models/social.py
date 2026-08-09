from pydantic import BaseModel, Field


class Social(BaseModel):
    github: str = Field(min_length=1)
    linkedin: str = Field(min_length=1)
    leetcode: str = Field(min_length=1)
    email: str = Field(min_length=1)