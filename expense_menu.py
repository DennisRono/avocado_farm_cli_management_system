from InquirerPy import prompt
from colorama import Fore
from main import (
    loading_simulation,
    session,
    get_choice,
    display_table,
    current_date,
)
from initialize_db import Avocado_Varieties, Expense


def expense_menu():
    options = ["1. Log Expense", "2. View Expenses", "3. Go Back"]
    print("\n".join(options))
    choice = get_choice()

    if choice == "1":
        log_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        return
    else:
        print(Fore.RED + "Invalid choice. Try again.")


def log_expense():

    varieties = session.query(Avocado_Varieties).all()

    if not varieties:
        print(Fore.RED + "No avocado varieties found. Please add varieties first.")
        return

    variety_choices = [variety.name for variety in varieties]
    questions = [
        {
            "type": "list",
            "name": "tree_type",
            "message": "Select Tree Variety:",
            "choices": variety_choices,
        },
        {
            "type": "input",
            "name": "quantity",
            "message": "Enter Quantity (number of avocado trees to plant):",
            "validate": lambda val: val.replace(".", "", 1).isdigit()
            or "Please enter a valid number.",
        },
        {
            "type": "input",
            "name": "cost",
            "message": "Enter cost per Avocado Tree:",
            "validate": lambda val: val.replace(".", "", 1).isdigit()
            or "Please enter a valid number.",
        },
        {
            "type": "input",
            "name": "description",
            "message": "Enter Description:",
            "validate": lambda val: val.strip() != "" or "Description cannot be empty.",
        },
    ]

    answers = prompt(questions)
    variety = answers["tree_type"]
    quantity = answers["quantity"]
    cost = float(answers["cost"])
    description = answers["description"]
    date = current_date()

    loading_simulation("Logging expense")

    try:
        new_expense = Expense(
            variety=variety,
            quantity=quantity,
            cost=cost,
            description=description,
            date=date,
        )
        session.add(new_expense)
        session.commit()
        print(Fore.GREEN + "Expense logged successfully.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        session.rollback()


def view_expenses():
    expenses = session.query(Expense).all()

    if not expenses:
        print(Fore.RED + "No expense records.")
    else:
        headers = ["Variety", "Quantity", "Cost", "Total Cost", "Description", "Date"]
        rows = [
            (
                exp.variety,
                exp.quantity,
                exp.cost,
                (float(exp.quantity) * float(exp.cost)),
                exp.description,
                exp.date,
            )
            for exp in expenses
        ]
        display_table(rows, headers)
