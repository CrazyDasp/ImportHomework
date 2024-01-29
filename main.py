from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import wikipedia



if __name__ == '__main__':
    get_employees('Федор')
    calculate_salary(30000)
    print(datetime.now(tz=None))
    print(wikipedia.page('Hybrid Theory').url)

