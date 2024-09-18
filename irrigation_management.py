from InquirerPy import prompt
from colorama import Fore
from main import (
    loading_simulation,
    session,
    get_choice,
    display_table,
    current_date,
)
from initialize_db import Irrigation


# Irrigation Management
def irrigation_menu():
    options = ["1. Log Irrigation", "2. View Irrigation Records", "3. Go Back"]
    print("\n".join(options))
    choice = get_choice()

    if choice == "1":
        log_irrigation()
    elif choice == "2":
        view_irrigation_records()
    elif choice == "3":
        return
    else:
        print(Fore.RED + "Invalid choice. Try again.")


def log_irrigation():
    questions = [
        {
            "type": "input",
            "name": "volume",
            "message": "Enter Water Volume (liters):",
            "validate": lambda val: val.replace(".", "", 1).isdigit()
            or "Please enter a valid number.",
        },
        {
            "type": "input",
            "name": "duration",
            "message": "Enter Duration (hours):",
            "validate": lambda val: val.replace(".", "", 1).isdigit()
            or "Please enter a valid number.",
        },
    ]

    answers = prompt(questions)
    volume = float(answers["volume"])
    duration = float(answers["duration"])
    date = current_date()

    loading_simulation("Logging irrigation")

    try:
        new_irrigation = Irrigation(volume=volume, duration=duration, date=date)
        session.add(new_irrigation)
        session.commit()
        print(Fore.GREEN + "Irrigation logged successfully.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        session.rollback()


def view_irrigation_records():
    irrigations = session.query(Irrigation).all()

    if not irrigations:
        print(Fore.RED + "No irrigation records.")
    else:
        headers = ["Volume (liters)", "Duration (hours)", "Date"]
        rows = [(irr.volume, irr.duration, irr.date) for irr in irrigations]
        display_table(rows, headers)
