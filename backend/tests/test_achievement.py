import pytest
from pydantic import ValidationError

from app.models.achievement import Achievement


def test_achievement():
    achievement = Achievement(
        description="Solved 900+ DSA problems on LeetCode."
    )

    assert achievement.description == "Solved 900+ DSA problems on LeetCode."


def test_achievement_rejects_empty_description():
    with pytest.raises(ValidationError):
        Achievement(description="")