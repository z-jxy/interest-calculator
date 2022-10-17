from datetime import date
from backend.functions import *
from backend.db import *


"""
Interest Calculator - @xzjxy
zjxy.00@gmail.com
09/29/2022

Calculating average daily balance
For each value found in the array of daily balances, 
the value gets added to the cycle_bal_tracker, 
we then set the adb to value of cycle bal tracker
"""

class profile:
    def __init__(self, daily_bals, apr=prime_rate) -> None:

        self.total_cycle_days = 30
        self.daily_bals = daily_bals
        self.apr = apr
        self.dpr = round(self.apr / 365, 5)
        self.date = date.today()

        self.balance_dates = [x for x in extract_date_values(balance_dates)]
        self.balance_day_count = diff_list_dates(self.balance_dates)
        self.balances = different_balances_incycle

        self.adb = get_adb(
            balance=different_balances_incycle, multiplier=self.balance_day_count
        )

        self.accrued_interest = round(
            (self.dpr * self.adb * self.total_cycle_days) / 100, 2
        )

    def get_cycle_interest(self):
        print(f"""
            At a daily percentage rate of {self.dpr}% \n
            Calculated from an APR of {self.apr}%, \n
            From the average daily balance of ${self.adb}, \n
            Your total interest charges for your cycle of {self.total_cycle_days} days is ${self.accrued_interest}!
            """
        )


poc = profile(cycle_to_date_data)
poc.get_cycle_interest()
