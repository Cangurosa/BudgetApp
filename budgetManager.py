import pandas as pd
from datetime import date
import os

class budgetManager:
    FILE = "budget-csv"

    def __init__(self):
        if not os.path.exists(self.FILE) or os.path.getsize(self.FILE) == 0:
            self.df = pd.DataFrame(colum=["obejct", "money", "date"])
        else:
            self.df = pd.read_csv(self.FILE)

    def add_entry(self, obj, money, date):
        new_row = {"object": obj, "money": money, "date": date}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_infex=True)
        self.save()

    def save(self):
        self.df.to_csv(self.FILE, index=False)