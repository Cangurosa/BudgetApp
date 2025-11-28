from BudgetManager import BudgetManager

def main():
    budget = BudgetManager()
    
    while True:
        tot = budget.df['money'].sum()
        spent = budget.df.loc[budget.df['money'] < 0, 'money'].sum()

        print("---BudgetManager---")
        print("Total budget: ", tot, "| Spent: ", spent,)
        print("1]--> Add expense")
        print("2]--> Add profit")
        print("3]--> Remove")
        print("4]--> Delete All")
        print("5]--> View")
        print("6]--> View All")
        print("?]--> Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            obj = input("Object: ")
            money = float(input("Money: "))
            date = input("Date[YYYY-MM-DD]: ")
            budget.add_entry(obj, -money, date)
            print(">Expense added!")

        elif choice == '2':
            obj = input("Object: ")
            money = float(input("Money: "))
            date = input("Date[YYYY-MM-DD]: ")
            budget.add_entry(obj, +money, date)
            print(">Profit added!")

        elif choice == '3':
            print(budget.df)
            res = int(input("What line you want to remove? "))
            budget.df.drop(index=res, inplace=True)
            print("Object removed!")


        elif choice == '4':
            res = input("Are you sure to delete all objects?[Y/N] ")
            if res == 'N' or res == 'n':
                continue
            else:
                budget.delete_all()
                print("All objects are done!")

        elif choice == '5':
            print("1. day")
            print("2. month")
            print("3. year")
            res = input("Choose a filter: ")

            if res == '1':
                day = int(input("day(1-31): "))
                rows = budget.df[budget.df["date"].dt.day == day]
                if rows.empty:
                    print("No objects in that day")
                else:
                    print(rows)
            
            if res == '2':
                month = int(input("month(1-12): "))
                rows = budget.df[budget.df["date"].dt.month == month]
                if rows.empty:
                    print("No objects in that day")
                else:
                    print(rows)

            if res == '3':
                year = input("year(YYYY): ")
                rows = budget.df[budget.df["date"].dt.year == year]
                if rows.empty:
                    print("No objects in that day")
                else:
                    print(rows)

        elif choice == '6':
            print(budget.df)
        
        elif choice == '?':
            print("Bye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
