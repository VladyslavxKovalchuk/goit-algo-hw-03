# Вимоги до завдання:

# Параметр функції users - це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
# Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
# Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').


from datetime import datetime
from datetime import date
from datetime import timedelta


def get_formated_workday(date: date):
    dayofweek = date.weekday() + 1
    print(dayofweek)
    if (dayofweek == 6) or (dayofweek == 7):
        return (date + timedelta(7 - dayofweek + 1)).strftime("%Y.%m.%d")
    return date.strftime("%Y.%m.%d")


def _is_leap(year):
    "year -> 1 if leap year, else 0."
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_next_birthday(birthday: date, fromdate: date):
    if (
        (_is_leap(birthday.year) == 1)
        and (_is_leap(fromdate.year) != 1)
        and (birthday.day == 29)
        and (birthday.month == 2)
    ):
        birthday_this_year = date(fromdate.year, 3, 1)
    else:
        birthday_this_year = date(fromdate.year, birthday.month, birthday.day)
    if birthday_this_year < fromdate:
        return get_next_birthday(birthday, date(fromdate.year + 1, 1, 1))
    return birthday_this_year


def get_upcoming_birthdays(users):
    today = date.today()
    upcomming_users_bday = []
    for user in users:
        user_bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        next_user_birthday = get_next_birthday(user_bday, today)

        diffcoef = (next_user_birthday - today).days
        if diffcoef in range(0, 7):
            upcomming_users_bday.append(
                {
                    "name": user["name"],
                    "congratulation_date": get_formated_workday(next_user_birthday),
                }
            )
    return upcomming_users_bday
