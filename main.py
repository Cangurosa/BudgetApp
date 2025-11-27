from BudgetManager import BudgetManager

def main():
    budget = BudgetManager()
    
    while True:
        print("---BudgetManager---")
        print("1]--> Add")
        print("2]--> Remove")
        print("3]--> Delete All")
        print("4]--> View")
        print("5]--> View All")
        print("?]--> Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            obj = input("Object: ")
            money = input("Money: ")
            date = input("Date[YYYY-MM-DD]: ")
            budget.add_entry(obj, money, date)
            print(">Entry added!")

        elif choice == '3':
            res = input("Are you sure to delete all objects?[Y/N] ")
            if res == 'N' or res == 'n':
                continue
            else:
                budget.delete_all()
                print("All objects are done!")

        elif choice == '4':
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

        elif choice == '5':
            print(budget.df)
        
        elif choice == '?':
            print("Bye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
