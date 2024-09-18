from InquirerPy import prompt
from colorama import Fore
from main import (
    loading_simulation,
    session,
    get_choice,
    display_table,
    current_date,
)
from initialize_db import Harvest
from tree_health_monitoring import select_tree


# Harvest Planning & Management
def harvest_menu():
    options = ["1. Log Harvest", "2. View Harvest Records", "3. Go Back"]
    print("\n".join(options))
    choice = get_choice()

    if choice == "1":
        log_harvest()
    elif choice == "2":
        view_harvest_records()
    elif choice == "3":
        return
    else:
        print(Fore.RED + "Invalid choice. Try again.")


def log_harvest():
    id = select_tree()[1]

    questions = [
        {
            "type": "input",
            "name": "quantity",
            "message": "Enter Quantity Harvested (kg):",
            "validate": lambda val: val.replace(".", "", 1).isdigit()
            or "Please enter a valid number.",
        },
    ]

    answers = prompt(questions)
    quantity = float(answers["quantity"])
    date = current_date()

    loading_simulation("Logging harvest")

    try:
        new_harvest = Harvest(tree_id=id, quantity=quantity, date=date)
        session.add(new_harvest)
        session.commit()
        print(Fore.GREEN + "Harvest logged successfully.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        session.rollback()


def view_harvest_records():
    harvests = session.query(Harvest).all()

    if not harvests:
        print(Fore.RED + "No harvest records.")
    else:
        headers = ["Tree ID", "Quantity", "Date"]
        rows = [(har.tree_id, har.quantity, har.date) for har in harvests]
        display_table(rows, headers)
