from typing import Union

card_number = input()
account_number = input()
"""Получаем данные карты от пользователя"""


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Возвращает замаскированный номер карты"""
    length_number = 16
    card_number = str(card_number)
    if len(card_number) == length_number:
        return f"{card_number[:4]}, {card_number[4:6]}**, ****, {card_number[-4:]}"
    return ""


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Возвращает замаскированный номер счета"""
    length_acc_number = 20
    account_number = str(account_number)
    if len(account_number) == length_acc_number:
        return f"**{account_number[-4:]}"
    return ""


print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
