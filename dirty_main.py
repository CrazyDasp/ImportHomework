from application.salary import *
from application.db.people import *
from datetime import *



if __name__ == '__main__':
    get_employees('Федор')
    calculate_salary(30000)
    print(datetime.now(tz=None))