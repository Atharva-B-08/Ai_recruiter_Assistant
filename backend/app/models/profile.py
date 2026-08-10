from pydantic import BaseModel, EmailStr, Field

class Profile(BaseModel):
    name: str = Field(min_length=1)
    title: str = Field(min_length=1)
    location: str = Field(min_length=1)
    country: str = Field(min_length=1)
    email: EmailStr
    phone: str = Field(min_length=1)
    summary: str = Field(min_length=1)
    open_to_work: bool
    preferred_roles: list[str] = Field(min_length=1)