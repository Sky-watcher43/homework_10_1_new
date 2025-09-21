import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("input_data, expected_result", [
    ("Maestro4567890123456789", "Maestro 4567 89** **** 6789"),
    ("счёт банка12345678901234567890", "счёт банка **7890"),
    ("Некорректная карта № abcdefghijkl", ""),
    ("Некорректный счёт № 1234567890123456789", "")
])
def test_mask_account_card(input_data, expected_result):
    assert mask_account_card(input_data) == expected_result


@pytest.mark.parametrize("date_string, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-31T23:59:59.999", "31.12.2023"),
    ("2024-02-29T00:00:00.000", "29.02.2024"),
])
def test_get_date(date_string, expected):
    assert get_date(date_string) == expected
