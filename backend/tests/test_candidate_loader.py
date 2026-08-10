from app.services.candidate_loader import load_candidate


def test_load_candidate():
    candidate = load_candidate()

    assert candidate.profile.name == "Atharva Butte"

    assert len(candidate.education) == 3

    assert len(candidate.experience) == 1

    assert candidate.skills.languages

    assert len(candidate.achievements) >= 1

    assert len(candidate.certificates) == 3

    assert candidate.socials.github

    assert len(candidate.projects) == 3