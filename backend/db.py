import numpy as np
import json
from datetime import date



current_date = "09/30/2022"
prime_rate = 25.74
cycle_days = 30


# Test data
cycle_to_date_data = """
{
    "Purchases": [
        {
            "Amount": "600.31",
            "Date": "09/02/2022"
        },
        {
            "Amount": "210.58",
            "Date": "09/12/2022"
        }
    ], 
    "Cycle": [
        {
            "Start": "08/15/2022",
            "End": "09/14/2022"
        }
    ],
    "StartingBalance": [
        {
            "Amount": "472.33"
        }
    ]
}
"""

posted_trxns = json.loads(cycle_to_date_data, parse_float="Purchases")
new_trxn = {"Amount": "50.33", "Date": "09/20/2022"}
posted_trxns["Purchases"].append(new_trxn)

a = np.array(posted_trxns)
b = posted_trxns["Purchases"][0:]
balances_in_cycle = np.array([x["Amount"] for x in b])
different_balances_incycle = [float(x) for x in balances_in_cycle]
balance_dates = [[x["Date"]] for x in b]
sum_of_bals = np.sum(balances_in_cycle.astype(float))
cur_bal = float(posted_trxns["StartingBalance"][0]["Amount"])
cycle_start = date(2022, 8, 30)
current_date = date(2022, 9, 30)
