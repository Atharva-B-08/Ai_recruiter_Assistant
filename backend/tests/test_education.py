from app.models.education import Education


def test_bachelor_education():
    education = Education(
        degree="Bachelor of Engineering",
        branch="Computer Engineering",
        college="Atharva College of Engineering",
        university="University of Mumbai",
        cgpa=8.18,
        percentage=72.31,
        status="Completed",
        start_year=2023,
        end_year=2026,
    )

    assert education.degree == "Bachelor of Engineering"
    assert education.cgpa == 8.18
    assert education.percentage == 72.31


def test_school_education_without_cgpa():
    education = Education(
        degree="10 th Standard",
        branch="",
        college="Saraswati Vidya Niketan",
        university="SSC State Board",
        percentage=88.2,
        status="Completed",
        start_year=2019,
        end_year=2021,
    )

    assert education.cgpa is None
    assert education.branch == ""
    assert education.percentage == 88.2