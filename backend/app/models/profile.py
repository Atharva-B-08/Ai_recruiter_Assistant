from pydantic import BaseModel, EmailStr

class Profile(BaseModel):
    name: str
    title: str
    location: str
    Country: str
    email: EmailStr
    phone: str
    summary: str
    open_to_work: bool
    preferred_roles: list[str]