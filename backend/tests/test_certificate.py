import pytest
from pydantic import ValidationError

from app.models.certificate import Certificate


def test_certificate():
    certificate = Certificate(
        name="Java Programming",
        issuer="",
        year="",
    )

    assert certificate.name == "Java Programming"
    assert certificate.issuer == ""
    assert certificate.year == ""


def test_certificate_rejects_empty_name():
    with pytest.raises(ValidationError):
        Certificate(
            name="",
            issuer="",
            year="",
        )