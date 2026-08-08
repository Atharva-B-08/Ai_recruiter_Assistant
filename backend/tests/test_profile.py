import pytest
from pydantic import ValidationError

from app.models.profile import Profile


def test_profile():
    profile = Profile(
        name="Atharva Butte",
        title="Backend Developer | Java Developer | Software Development Engineer",
        location="Mumbai, Maharashtra, India",
        Country="India",
        email="butteatharva2005@gmail.com",
        phone="+91 9619849620",
        summary=(
            "I'm a Computer Engineering student passionate about backend "
            "development, Java, Spring Boot, cloud computing, and building "
            "scalable web applications."
        ),
        open_to_work=True,
        preferred_roles=[
            "Software Development Engineer",
            "Backend Developer",
            "Java Developer",
            "Full Stack Developer",
        ],
    )

    assert profile.name == "Atharva Butte"
    assert profile.open_to_work is True
    assert len(profile.preferred_roles) == 4


def test_profile_rejects_invalid_email():
    with pytest.raises(ValidationError):
        Profile(
            name="Atharva Butte",
            title="Backend Developer",
            location="Mumbai, Maharashtra, India",
            Country="India",
            email="invalid-email",
            phone="+91 9619849620",
            summary="Backend developer",
            open_to_work=True,
            preferred_roles=["Backend Developer"],
        )

def test_profile_rejects_empty_name():
    with pytest.raises(ValidationError):
        Profile(
            name="",
            title="Backend Developer",
            location="Mumbai, Maharashtra, India",
            Country="India",
            email="butteatharva2005@gmail.com",
            phone="+91 9619849620",
            summary="Backend developer",
            open_to_work=True,
            preferred_roles=["Backend Developer"],
        )