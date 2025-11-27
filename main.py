def main():
    budget = budgetManager()
    
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

        elif choice == '4':
            print("1. day")
            print("2. month")
            print("3. year")
            

        elif choice == '5':
            print(budget.df)
        
        elif choice == '?':
            print("Bye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
