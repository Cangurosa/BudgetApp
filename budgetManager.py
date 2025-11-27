import pandas as pd
from datetime import date
import os

class BudgetManager:
    FILE = "budget.csv"

    def __init__(self):
        if not os.path.exists(self.FILE) or os.path.getsize(self.FILE) == 0:
            self.df = pd.DataFrame(columns=["object", "money", "date"])
        else:
            self.df = pd.read_csv(self.FILE)
            self.df["date"] = pd.to_datetime(self.df["date"], errors="coerce")

    def add_entry(self, obj, money, date):
        new_row = {"object": obj, "money":float(money), "date": pd.to_datetime(date)}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        self.save()

    def save(self):
        self.df.to_csv(self.FILE, index=False)

    def delete_all(self):
        self.df = pd.DataFrame(columns = self.df.columns)
        self.save()