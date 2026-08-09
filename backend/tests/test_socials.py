import pytest
from pydantic import ValidationError

from app.models.social import Social


def test_social():
    social = Social(
        github="https://github.com/Atharva-B-08",
        linkedin="[https://www.linkedin.com/in/atharva-butte-b0248a2b5/](https://www.linkedin.com/in/atharva-butte-b0248a2b5/)",
        leetcode="[https://leetcode.com/u/butteatharva2005/](https://leetcode.com/u/butteatharva2005/)",
        email="[butteatharva2005@gmail.com](mailto:butteatharva2005@gmail.com)",
    )

    assert "github.com" in social.github
    assert "linkedin.com" in social.linkedin
    assert "leetcode.com" in social.leetcode
    assert "gmail.com" in social.email


def test_social_rejects_empty_github():
    with pytest.raises(ValidationError):
        Social(
            github="",
            linkedin="linkedin",
            leetcode="leetcode",
            email="email",
        )