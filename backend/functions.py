import numpy as np
from backend.db import *


def balance_tracker(purchases):
    c = cur_bal
    for x in purchases:
        c += x
    return round(c, 2)


def extract_date_values(data):
    for x in data:
        split = x[0].split("/")
        day = int(split[1])
        yield day


def find_cycstart_to_curdate():
    value = int(current_date.day) - int(cycle_start.day)
    if value == 0:
        if int(current_date.month) == int(cycle_start.month) + 1:
            value = 30
        elif int(current_date.month) > int(cycle_start.month):
            value = "your cycle should be available by now :/"
    return value


def daily_bal_diff(start_day, next_bal_day):
    if start_day < next_bal_day:
        number_of_days = next_bal_day - start_day
    else:
        number_of_days = start_day - next_bal_day

    if number_of_days == 0:
        if int(current_date.month) == int(cycle_start.month) + 1:
            number_of_days = 30
        elif int(current_date.month) > int(cycle_start.month):
            number_of_days = "your cycle should be printed by now :/"
    return number_of_days

def calc_date_balances():
    cycle_max = 30
    days_in_cycle = 0
    current_day = current_date.day
    if days_in_cycle != cycle_max:
        for day in range(cycle_max):
            days_in_cycle = +1


def diff_list_dates(list=[]):
    # add in later
    # date = datetime.today()
    y = len(list)
    count = 0
    def diff_helper(count):
        if count != (len(list) - 1):
            for x in list:
                if x != list[-1]:
                    diff = daily_bal_diff(x, list[(count + 1)])
                    count = +1
                    yield diff
                else:
                    last_diff = daily_bal_diff(x, int(30))
                    count = +1
                    yield last_diff

    final = [x for x in diff_helper(count)]
    return final


def adb_calculator(f):
    def wrapper(*args, **kwargs):
        final_adb = (np.sum([_ for _ in f(*args, **kwargs)])) / 30
        final_adb = round(final_adb, 2)
        return final_adb
    return wrapper


@adb_calculator
def get_adb(balance, multiplier):
    _ = 0
    for x in balance:
        value = x * multiplier[_]
        yield value
