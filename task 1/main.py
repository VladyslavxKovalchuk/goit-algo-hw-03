# Cтворіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

# Вимоги до завдання:
# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.

from datetime import datetime


def get_days_from_today(date):
    today = datetime.today()
    try:
        datedt = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(
            "parametr date must be in format yyyy-mm-dd. example: "
            + today.strftime("%Y-%m-%d")
        )
        return
    period = today - datedt
    return period.days
