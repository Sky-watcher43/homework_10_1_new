import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('expected', ['8764 90** **** 2653'])
def test_get_mask_card_number(mask_card_number, expected) -> None:
    assert get_mask_card_number(mask_card_number) == expected


def test_get_mask_account(mask_account) -> None:
    assert get_mask_account(mask_account) == '**9643'


def test_get_mask_card_number_empty(error_number) -> None:
    assert get_mask_card_number(error_number) == ''


def test_get_mask_account_empty(error_number) -> None:
    assert get_mask_account(error_number) == ''
