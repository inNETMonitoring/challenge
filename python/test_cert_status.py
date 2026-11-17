import pytest

from cert_status import classify_cert


@pytest.mark.parametrize(
    "days_left, expected",
    [
        (90, "OK"),
        (31, "OK"),
        (30, "WARN"),
        (8, "WARN"),
        (7, "CRIT"),
        (0, "CRIT"),
        (-1, "EXPIRED"),
        (-365, "EXPIRED"),
    ],
)
def test_classify_cert(days_left, expected):
    assert classify_cert(days_left) == expected


def test_classify_cert_without_date_is_unknown():
    assert classify_cert(None) == "UNKNOWN"
