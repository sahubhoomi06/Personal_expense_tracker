print("1. Add Expense \n2. View Expense \n3. Total Spending \n4. Category Summary \n5. Highest Expense\n6. Exit")

Expenses = []


def add_exp():
    print("------Add Expense------")

    name = input("Enter Expense Name: ")
    amount = int(input("Enter Expense Amount: "))
    category = input("Enter Category: ")
    date = input("Enter Date: ")

    expense1 = {
        'name': name,
        'amount': amount,
        'category': category,
        'date': date
    }

    Expenses.append(expense1)


def view_exp():
    print("\n------All Expenses------")

    for expense in Expenses:
        print("Name:", expense['name'])
        print("Amount:", expense['amount'])
        print("Category:", expense['category'])
        print("Date:", expense['date'])
        print("----------------------")


def total():
    Total = 0

    for expense in Expenses:
        Total = Total + expense['amount']

    print("Total Spending:", Total)


def cat_sum():
    Food = 0
    Transport = 0
    Others = 0

    print("\n----Category Summary----")

    print("\n---Food Expense---")

    for expense in Expenses:

        if expense['category'] == "Food":
            print("Name:", expense['name'])
            print("Amount:", expense['amount'])
            print("Date:", expense['date'])

            Food = Food + expense['amount']

    print("Food Total:", Food)

    print("\n---Transport Expense---")

    for expense in Expenses:

        if expense['category'] == "Transport":
            print("Name:", expense['name'])
            print("Amount:", expense['amount'])
            print("Date:", expense['date'])

            Transport = Transport + expense['amount']

    print("Transport Total:", Transport)

    print("\n---Other Expense---")

    for expense in Expenses:

        if expense['category'] != "Food" and expense['category'] != "Transport":
            print("Name:", expense['name'])
            print("Amount:", expense['amount'])
            print("Date:", expense['date'])

            Others = Others + expense['amount']

    print("Others Total:", Others)


def highest_exp():

    if Expenses == []:
        print("No expenses found.")
        return

    highest = Expenses[0]

    for expense in Expenses:
        if expense['amount'] > highest['amount']:
            highest = expense

    print("------Highest Expense------")
    print("Name:", highest['name'])
    print("Amount:", highest['amount'])
    print("Category:", highest['category'])
    print("Date:", highest['date'])


choice = input("Enter your choice: ")

while choice != "6":

    if choice == "1":
        add_exp()

    elif choice == "2":
        view_exp()

    elif choice == "3":
        total()

    elif choice == "4":
        cat_sum()

    elif choice == "5":
        highest_exp()

    else:
        print("Invalid Choice!")

    choice = input("Enter your choice: ")

print("Program Exited.")