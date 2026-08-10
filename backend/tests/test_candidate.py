from app.models.candidate import CandidateProfile


def test_candidate_profile():
    candidate = CandidateProfile(
        profile={
            "name": "Atharva Butte",
            "title": "Backend Developer | Java Developer | Software Development Engineer",
            "location": "Mumbai, Maharashtra, India",
            "country": "India",
            "email": "butteatharva2005@gmail.com",
            "phone": "+91 9619849620",
            "summary": (
                "I'm a Computer Engineering student passionate about "
                "backend development, Java, Spring Boot, cloud computing, "
                "and building scalable web applications."
            ),
            "open_to_work": True,
            "preferred_roles": [
                "Software Development Engineer",
                "Backend Developer",
                "Java Developer",
                "Full Stack Developer",
            ],
        }, # type: ignore

        education=[],

        experience=[],

        skills={
            "languages": ["Java", "Python"],
            "backend": ["Spring Boot", "Node.js"],
            "frontend": ["React", "JavaScript"],
            "database": ["MySQL", "PostgreSQL"],
            "messaging_platforms": ["Kafka"],
            "tools": ["Postman", "IntelliJ IDEA"],
            "cloud": ["Vercel", "Supabase"],
            "version_control": ["Git", "GitHub"],
            "other": [],
        }, # type: ignore

        achievements=[],

        certificates=[],

        socials={
            "github": "https://github.com/Atharva-B-08",
            "linkedin": "https://www.linkedin.com/in/atharva-butte-b0248a2b5/",
            "leetcode": "https://leetcode.com/u/butteatharva2005/",
            "email": "butteatharva2005@gmail.com",
        }, # type: ignore

        projects=[],
    )

    assert candidate.profile.name == "Atharva Butte"
    assert candidate.skills.backend[0] == "Spring Boot"
    assert candidate.skills.database[0] == "MySQL"
    assert candidate.socials.github == "https://github.com/Atharva-B-08"
    assert candidate.projects == []