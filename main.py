from application.db.people import get_employees
from application.salary import calculate_salary

import datetime


def year_today():
    now = datetime.datetime.now()
    return now.date()


if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
    print(year_today())