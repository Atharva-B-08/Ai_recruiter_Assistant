from app.models.skills import Skills


def test_skills():
    skills = Skills(
        languages=["Java", "Python", "JavaScript", "SQL"],
        backend=[
            "Spring Boot",
            "Spring MVC",
            "Spring Security",
            "Hibernate",
            "JPA",
            "REST APIs",
            "JWT",
        ],
        frontend=[
            "React",
            "HTML",
            "CSS",
            "Tailwind CSS",
        ],
        database=[
            "MySQL",
            "PostgreSQL",
        ],
        messaging_platforms=["kafka"],
        tools=[
            "Git",
            "GitHub",
            "Postman",
            "IntelliJ IDEA",
            "VS Code",
        ],
        cloud=[
            "Vercel",
            "Supabase",
            "Docker",
        ],
        version_control=[
            "GitHub",
            "git",
        ],
        other=[
            "Agile Methodology",
        ],
    )

    assert "Java" in skills.languages
    assert "Spring Boot" in skills.backend
    assert "React" in skills.frontend
    assert "MySQL" in skills.database
    assert "kafka" in skills.messaging_platforms
    assert "Docker" in skills.cloud