from app.models.experience import Experience


def test_fresher_experience():
    experience = Experience(
        company="",
        position="Fresher",
        duration="",
        description=(
            "No professional experience yet. Built multiple academic "
            "and personal full-stack projects."
        ),
        Opportunity=(
            "Looking for an entry-level position in software development, "
            "where I can apply my skills and contribute to the growth "
            "of the organization."
        ),
    )

    assert experience.position == "Fresher"
    assert experience.company == ""
    assert experience.duration == ""
    assert "No professional experience" in experience.description