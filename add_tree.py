from colorama import Fore
from InquirerPy import prompt
from main import (
    loading_simulation,
    session,
    get_choice,
    get_input,
    display_table,
    current_date,
)
from initialize_db import Avocado_Varieties, Tree


def new_tree_opts():
    options = [
        "1. Add a New Variety",
        "2. Update a Variety",
        "3. Add a Tree",
        "4. View Varieties",
        "5. View Trees",
        "6. Go Back",
    ]
    print("\n".join(options))
    choice = get_choice()

    if choice == "1":
        add_new_variety()
    elif choice == "2":
        update_variety()
    elif choice == "3":
        add_tree()
    elif choice == "4":
        view_varieties()
    elif choice == "5":
        view_trees()
    elif choice == "6":
        return
    else:
        print(Fore.RED + "Invalid choice. Try again.")


def add_new_variety():
    name = get_input("Enter Avocado Variety Name")

    loading_simulation("Adding new variety")

    new_variety = Avocado_Varieties(name=name)
    session.add(new_variety)
    session.commit()

    print(Fore.GREEN + f"Variety '{name}' added successfully.")


def update_variety():
    varieties = session.query(Avocado_Varieties).all()

    if not varieties:
        return

    variety_choices = [
        {"name": f"{variety.id}: {variety.name}", "value": variety.id}
        for variety in varieties
    ]

    questions = [
        {
            "type": "list",
            "name": "selected_variety_id",
            "message": "Select the variety you want to update:",
            "choices": variety_choices,
        },
        {
            "type": "input",
            "name": "new_name",
            "message": "Enter new name for the variety (Leave blank to keep current name):",
        },
    ]

    answers = prompt(questions)
    selected_variety_id = answers["selected_variety_id"]
    new_name = answers["new_name"]

    variety = session.query(Avocado_Varieties).filter_by(id=selected_variety_id).first()

    if variety:
        if new_name:
            variety.name = new_name
            session.commit()
            print(Fore.GREEN + f"Variety updated to '{new_name}'.")
        else:
            print(Fore.YELLOW + "No changes made.")
    else:
        print(Fore.RED + "Variety not found.")


def view_varieties():
    varieties = session.query(Avocado_Varieties).all()

    if not varieties:
        print(Fore.RED + "No avocado varieties found.")
    else:
        headers = ["ID", "Name"]
        rows = [(var.id, var.name) for var in varieties]
        display_table(rows, headers)


def add_tree():

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
            "name": "height",
            "message": "Enter Tree Height:",
            "validate": lambda val: val.replace(".", "", 1).isdigit()
            or "Please enter a valid number.",
        },
        {
            "type": "list",
            "name": "leaf_health",
            "message": "Enter Leaf Health Status:",
            "choices": ["Good", "Fair", "Poor"],
        },
        {
            "type": "input",
            "name": "age",
            "message": "Enter Tree Age (in years):",
            "validate": lambda val: val.isdigit() or "Please enter a valid age.",
        },
        {
            "type": "input",
            "name": "diameter",
            "message": "Enter Tree Diameter (in meters):",
            "validate": lambda val: val.replace(".", "", 1).isdigit()
            or "Please enter a valid diameter.",
        },
        {
            "type": "confirm",
            "name": "pest_infested",
            "message": "Is the tree pest infested?",
            "default": False,
        },
    ]

    answers = prompt(questions)

    height = float(answers["height"])
    tree_type = answers["tree_type"]
    leaf_health = answers["leaf_health"]
    age = int(answers["age"])
    diameter = float(answers["diameter"])
    pest_infested = answers["pest_infested"]

    loading_simulation("Adding tree")

    new_tree = Tree(
        height=height,
        variety=tree_type,
        leaf_health=leaf_health,
        age=age,
        diameter=diameter,
        pest_infested=pest_infested,
        date=current_date(),
    )
    session.add(new_tree)
    session.commit()

    print(Fore.GREEN + f"Tree with type '{tree_type}' added successfully.")


def view_trees():
    trees = session.query(Tree).all()

    if not trees:
        print(Fore.RED + "No trees found.")
    else:
        headers = [
            "ID",
            "Variety",
            "Height",
            "Leaf Health",
            "Age",
            "Diameter",
            "Pest Infested",
            "Date",
        ]
        rows = [
            (
                tree.id,
                tree.variety,
                tree.height,
                tree.leaf_health,
                tree.age,
                tree.diameter,
                "Yes" if tree.pest_infested else "No",
                tree.date,
            )
            for tree in trees
        ]
        display_table(rows, headers)
