from pydantic import BaseModel

from app.models.profile import Profile
from app.models.education import Education
from app.models.experience import Experience
from app.models.skills import Skills
from app.models.achievement import Achievement
from app.models.certificate import Certificate
from app.models.social import Social
from app.models.project import Project


class CandidateProfile(BaseModel):
    profile: Profile
    education: list[Education]
    experience: list[Experience]
    skills: Skills
    achievements: list[Achievement]
    certificates: list[Certificate]
    socials: Social
    projects: list[Project]