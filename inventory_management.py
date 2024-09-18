from InquirerPy import prompt
from colorama import Fore
from main import (
    loading_simulation,
    session,
    get_choice,
    display_table,
    current_date,
)
from initialize_db import Inventory


def inventory_menu():
    options = ["1. Log Inventory", "2. View Inventory", "3. Go Back"]
    print("\n".join(options))
    choice = get_choice()

    if choice == "1":
        log_inventory()
    elif choice == "2":
        view_inventory()
    elif choice == "3":
        return
    else:
        print(Fore.RED + "Invalid choice. Try again.")


def log_inventory():
    questions = [
        {
            "type": "input",
            "name": "quantity",
            "message": "Enter Quantity (kg):",
            "validate": lambda val: val.replace(".", "", 1).isdigit()
            or "Please enter a valid number.",
        },
        {
            "type": "list",
            "name": "size",
            "message": "Enter Size:",
            "choices": ["small", "medium", "large"],
        },
        {
            "type": "list",
            "name": "quality",
            "message": "Enter Quality:",
            "choices": ["Good", "Fair", "Poor"],
        },
    ]

    answers = prompt(questions)
    quantity = float(answers["quantity"])
    size = answers["size"]
    quality = answers["quality"]
    date = current_date()

    loading_simulation("Logging inventory")

    try:
        new_inventory = Inventory(
            quantity=quantity, size=size, quality=quality, date=date
        )
        session.add(new_inventory)
        session.commit()
        print(Fore.GREEN + "Inventory logged successfully.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        session.rollback()


def view_inventory():
    inventory = session.query(Inventory).all()

    if not inventory:
        print(Fore.RED + "No inventory records.")
    else:
        headers = ["Quantity", "Size", "Quality", "Date"]
        rows = [(inv.quantity, inv.size, inv.quality, inv.date) for inv in inventory]
        display_table(rows, headers)
