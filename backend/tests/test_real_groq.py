import os

import pytest

from app.services.groq_service import GroqService


@pytest.mark.skipif(
    not os.getenv("GROQ_API_KEY"),
    reason="GROQ_API_KEY is not configured",
)
def test_real_groq_answer():
    service = GroqService()

    answer = service.generate_answer(
        question="Tell me about your FinTrack project.",
        candidate_context="""
        Name: Atharva Butte.

        FinTrack is a full-stack personal finance management
        application.

        Technologies:
        Java, Spring Boot, Spring Security, Spring Data JPA,
        Hibernate, JWT Authentication, React, PostgreSQL,
        and Supabase.

        Features include:
        budget management, income tracking, expense tracking,
        analytics dashboard, multiple accounts,
        recurring transactions, receipt upload, and REST APIs.

        Atharva's contribution included backend architecture,
        REST APIs, JWT authentication and authorization,
        PostgreSQL database design, and frontend-backend integration.
        """,
    )

    assert isinstance(answer, str)
    assert len(answer.strip()) > 0

    print("\nReal Groq answer:")
    print(answer)