from sqlalchemy import func
from colorama import Fore, Style
from InquirerPy import prompt
from tabulate import tabulate
from main import session
from initialize_db import (
    Avocado_Varieties,
    Tree,
    Irrigation,
    Harvest,
    Inventory,
    Expense,
    Sale,
    Distribution,
)


main_menu_choices = [
    {"name": "Generate Tree Health Report", "value": "tree_health"},
    {"name": "Generate Harvest Report", "value": "harvest_report"},
    {"name": "Generate Sales Report", "value": "sales_report"},
    {"name": "Generate Expense Report", "value": "expense_report"},
    {"name": "Exit", "value": "exit"},
]


def generate_tree_health_report():
    trees = session.query(Tree).all()
    healthy_count = sum(
        1 for tree in trees if tree.leaf_health == "Good" and not tree.pest_infested
    )
    unhealthy_count = len(trees) - healthy_count
    table_data = [
        ["Total Trees", len(trees)],
        ["Healthy Trees", healthy_count],
        ["Unhealthy Trees", unhealthy_count],
    ]
    print(f"\n{Fore.GREEN}Tree Health Report{Style.RESET_ALL}")
    print(tabulate(table_data, headers=["Metric", "Count"], tablefmt="fancy_grid"))
    if unhealthy_count > 0:
        unhealthy_trees_data = [
            [tree.id, tree.leaf_health, tree.pest_infested]
            for tree in trees
            if tree.leaf_health != "Good" or tree.pest_infested
        ]
        print(f"\n{Fore.RED}List of Unhealthy Trees:")
        print(
            tabulate(
                unhealthy_trees_data,
                headers=["Tree ID", "Leaf Health", "Pest Infested"],
                tablefmt="fancy_grid",
            )
        )


def generate_harvest_report():
    total_quantity = session.query(func.sum(Harvest.quantity)).scalar() or 0
    recent_harvest = session.query(Harvest).order_by(Harvest.date.desc()).first()
    table_data = [["Total Harvested Quantity", f"{total_quantity} kg"]]
    if recent_harvest:
        table_data.append(
            [
                "Most Recent Harvest",
                f"{recent_harvest.quantity} kg on {recent_harvest.date}",
            ]
        )
    print(f"\n{Fore.GREEN}Harvest Report{Style.RESET_ALL}")
    print(tabulate(table_data, headers=["Metric", "Details"], tablefmt="fancy_grid"))


def generate_sales_report():
    total_sales = session.query(func.sum(Sale.quantity)).scalar() or 0
    total_revenue = session.query(func.sum(Sale.quantity * Sale.price)).scalar() or 0
    table_data = [
        ["Total Sales Quantity", f"{total_sales} kg"],
        ["Total Revenue", f"${total_revenue:.2f}"],
    ]
    print(f"\n{Fore.GREEN}Sales Report{Style.RESET_ALL}")
    print(tabulate(table_data, headers=["Metric", "Details"], tablefmt="fancy_grid"))
    top_buyers = (
        session.query(Sale.buyer_name, func.sum(Sale.quantity))
        .group_by(Sale.buyer_name)
        .order_by(func.sum(Sale.quantity).desc())
        .all()
    )
    if top_buyers:
        top_buyers_data = [[buyer, quantity] for buyer, quantity in top_buyers]
        print(f"\n{Fore.GREEN}Top Buyers:")
        print(
            tabulate(
                top_buyers_data,
                headers=["Buyer", "Quantity Purchased (kg)"],
                tablefmt="fancy_grid",
            )
        )


def generate_expense_report():
    total_expenses = session.query(func.sum(Expense.cost)).scalar() or 0
    recent_expense = session.query(Expense).order_by(Expense.date.desc()).first()
    table_data = [["Total Expenses", f"${total_expenses:.2f}"]]
    if recent_expense:
        table_data.append(
            [
                "Most Recent Expense",
                f"${recent_expense.cost:.2f} on {recent_expense.date} ({recent_expense.description})",
            ]
        )
    print(f"\n{Fore.GREEN}Expense Report{Style.RESET_ALL}")
    print(tabulate(table_data, headers=["Metric", "Details"], tablefmt="fancy_grid"))


def reports_menu():
    while True:
        answers = prompt(
            [
                {
                    "type": "list",
                    "name": "menu_choice",
                    "message": "Select a report to generate:",
                    "choices": main_menu_choices,
                }
            ]
        )
        if answers["menu_choice"] == "tree_health":
            generate_tree_health_report()
        elif answers["menu_choice"] == "harvest_report":
            generate_harvest_report()
        elif answers["menu_choice"] == "sales_report":
            generate_sales_report()
        elif answers["menu_choice"] == "expense_report":
            generate_expense_report()
        elif answers["menu_choice"] == "exit":
            print(f"{Fore.GREEN}Exiting the application.")
            break

        # Pause for user input to continue
        input(f"\n{Fore.YELLOW}Press Enter to return to the main menu...")
