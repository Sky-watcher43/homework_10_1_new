from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number

card_account = input().lower()
date = input().lower()
"""Получаем данные от пользователя"""


def mask_account_card(card_account: str) -> str:
    """Обрабатывает информацию о картах и о счетах"""
    if "счет" in card_account or "счёт" in card_account:
        if card_account[-20:].isdigit():
            number_account = card_account[-20:]
            masked_account = get_mask_account(number_account)
            return f"{card_account[:-20]} {masked_account}"
    else:
        if card_account[-16:].isdigit():
            number_card = card_account[-16:]
            masked_card = get_mask_card_number(number_card)
            return f"{card_account[:-16]} {masked_card}"
    return''


result = mask_account_card(card_account)
print(result)


def get_date(date: str) -> str:
    """Возвращает отформатированную строку с датой"""
    string_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return string_date.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
