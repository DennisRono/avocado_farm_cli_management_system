from InquirerPy import prompt
from colorama import Fore
from main import (
    get_choice,
    loading_simulation,
    session,
    current_date,
    display_table,
)
from initialize_db import Tree


# Tree Health Monitoring
def tree_health_menu():
    options = ["1. Log Tree Health", "2. View Tree Health Records", "3. Go Back"]
    print("\n".join(options))
    choice = get_choice()

    if choice == "1":
        log_tree_health()
    elif choice == "2":
        view_tree_health_records()
    elif choice == "3":
        return
    else:
        print(Fore.RED + "Invalid choice. Try again.")


def select_tree():
    """Function to display a CLI choice selector for trees."""
    trees = session.query(Tree).all()

    if not trees:
        print(Fore.RED + "No trees available in the database.")
        return None

    # Prepare tree options for selection
    tree_choices = [
        (
            f"Tree ID: {tree.id} | Height: {tree.height}m | Leaf Health: {tree.leaf_health}",
            tree.id,
        )
        for tree in trees
    ]

    # Use InquirerPy to prompt the user for a tree selection
    question = [
        {
            "type": "list",
            "name": "tree",
            "message": "Select a Tree",
            "choices": tree_choices,
        }
    ]

    answer = prompt(question)
    return answer["tree"] if answer else None


def log_tree_health():
    id = select_tree()[1]

    if id is None:
        print(Fore.RED + "No tree selected. Aborting operation.")
        return

    # Use InquirerPy to get updated tree health details
    questions = [
        {
            "type": "input",
            "name": "height",
            "message": "Enter Updated Height (meters):",
            "validate": lambda val: val.replace(".", "", 1).isdigit()
            or "Please enter a valid number.",
        },
        {
            "type": "list",
            "name": "leaf_health",
            "message": "Enter Updated Leaf Health:",
            "choices": ["Good", "Fair", "Poor"],
        },
    ]

    answers = prompt(questions)
    height = answers["height"]
    leaf_health = answers["leaf_health"]
    date = current_date()

    loading_simulation("Logging tree health")

    try:
        # Update the selected tree's health data
        tree = session.query(Tree).filter_by(id=id).first()
        if tree:
            if height:
                tree.height = float(height)
            tree.leaf_health = leaf_health
            tree.date = date
            session.commit()
            print(Fore.GREEN + "Tree health logged successfully.")
        else:
            print(Fore.RED + "Tree not found in the database.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        session.rollback()


def view_tree_health_records():
    trees = session.query(Tree).all()

    if not trees:
        print(Fore.RED + "No tree health records.")
    else:
        headers = ["Tree ID", "Height (m)", "Leaf Health", "Date"]
        rows = [(tree.id, tree.height, tree.leaf_health, tree.date) for tree in trees]
        display_table(rows, headers)
