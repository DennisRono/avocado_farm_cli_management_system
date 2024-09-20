from datetime import date
from main import session
from initialize_db import (
    Avocado_Varieties,
    Distribution,
    Expense,
    Harvest,
    Inventory,
    Irrigation,
    Sale,
    Tree,
)


varieties = [
    Avocado_Varieties(name="Hass"),
    Avocado_Varieties(name="Fuerte"),
    Avocado_Varieties(name="Bacon"),
    Avocado_Varieties(name="Zutano"),
    Avocado_Varieties(name="Reed"),
    Avocado_Varieties(name="Lamb Hass"),
    Avocado_Varieties(name="Pinkerton"),
    Avocado_Varieties(name="Gwen"),
    Avocado_Varieties(name="Sharwil"),
    Avocado_Varieties(name="Mexicola"),
]


trees = [
    Tree(
        height=5.6,
        variety="Hass",
        leaf_health="Healthy",
        age=5,
        diameter=0.8,
        pest_infested=False,
        date=date(2023, 5, 12),
    ),
    Tree(
        height=4.8,
        variety="Fuerte",
        leaf_health="Moderate",
        age=7,
        diameter=0.9,
        pest_infested=True,
        date=date(2023, 6, 5),
    ),
    Tree(
        height=6.2,
        variety="Bacon",
        leaf_health="Healthy",
        age=3,
        diameter=0.7,
        pest_infested=False,
        date=date(2023, 7, 14),
    ),
    Tree(
        height=3.4,
        variety="Zutano",
        leaf_health="Poor",
        age=2,
        diameter=0.5,
        pest_infested=True,
        date=date(2023, 8, 2),
    ),
    Tree(
        height=5.1,
        variety="Reed",
        leaf_health="Healthy",
        age=6,
        diameter=0.8,
        pest_infested=False,
        date=date(2023, 8, 20),
    ),
    Tree(
        height=4.7,
        variety="Lamb Hass",
        leaf_health="Moderate",
        age=4,
        diameter=0.6,
        pest_infested=True,
        date=date(2023, 9, 1),
    ),
    Tree(
        height=5.9,
        variety="Pinkerton",
        leaf_health="Healthy",
        age=8,
        diameter=0.9,
        pest_infested=False,
        date=date(2023, 9, 10),
    ),
    Tree(
        height=6.3,
        variety="Gwen",
        leaf_health="Moderate",
        age=7,
        diameter=1.0,
        pest_infested=True,
        date=date(2023, 9, 15),
    ),
    Tree(
        height=4.5,
        variety="Sharwil",
        leaf_health="Poor",
        age=3,
        diameter=0.6,
        pest_infested=False,
        date=date(2023, 9, 25),
    ),
    Tree(
        height=5.8,
        variety="Mexicola",
        leaf_health="Healthy",
        age=5,
        diameter=0.9,
        pest_infested=False,
        date=date(2023, 10, 5),
    ),
]


irrigations = [
    Irrigation(volume=100.5, duration=30.0, date=date(2023, 5, 12)),
    Irrigation(volume=150.0, duration=45.0, date=date(2023, 5, 15)),
    Irrigation(volume=120.5, duration=35.0, date=date(2023, 6, 10)),
    Irrigation(volume=130.5, duration=40.0, date=date(2023, 6, 20)),
    Irrigation(volume=110.0, duration=32.0, date=date(2023, 7, 5)),
    Irrigation(volume=140.0, duration=42.0, date=date(2023, 7, 18)),
    Irrigation(volume=125.5, duration=38.0, date=date(2023, 8, 8)),
    Irrigation(volume=115.5, duration=34.0, date=date(2023, 8, 15)),
    Irrigation(volume=135.0, duration=41.0, date=date(2023, 9, 10)),
    Irrigation(volume=145.0, duration=43.0, date=date(2023, 9, 20)),
]


harvests = [
    Harvest(tree_id="1", quantity=15.5, date=date(2023, 5, 12)),
    Harvest(tree_id="2", quantity=10.0, date=date(2023, 5, 20)),
    Harvest(tree_id="3", quantity=20.5, date=date(2023, 6, 5)),
    Harvest(tree_id="4", quantity=18.0, date=date(2023, 6, 10)),
    Harvest(tree_id="5", quantity=12.5, date=date(2023, 7, 1)),
    Harvest(tree_id="6", quantity=22.5, date=date(2023, 7, 15)),
    Harvest(tree_id="7", quantity=17.0, date=date(2023, 8, 1)),
    Harvest(tree_id="8", quantity=19.5, date=date(2023, 8, 20)),
    Harvest(tree_id="9", quantity=21.0, date=date(2023, 9, 1)),
    Harvest(tree_id="10", quantity=25.0, date=date(2023, 9, 10)),
]


inventories = [
    Inventory(quantity=10.5, size="Small", quality="A", date=date(2023, 5, 15)),
    Inventory(quantity=15.0, size="Medium", quality="B", date=date(2023, 6, 10)),
    Inventory(quantity=12.0, size="Large", quality="A", date=date(2023, 6, 20)),
    Inventory(quantity=18.5, size="Small", quality="B", date=date(2023, 7, 1)),
    Inventory(quantity=14.5, size="Medium", quality="A", date=date(2023, 7, 15)),
    Inventory(quantity=20.5, size="Large", quality="B", date=date(2023, 8, 10)),
    Inventory(quantity=16.0, size="Small", quality="A", date=date(2023, 8, 20)),
    Inventory(quantity=13.5, size="Medium", quality="B", date=date(2023, 9, 5)),
    Inventory(quantity=22.0, size="Large", quality="A", date=date(2023, 9, 15)),
    Inventory(quantity=25.5, size="Small", quality="B", date=date(2023, 10, 1)),
]


expenses = [
    Expense(
        variety="Hass",
        quantity=10.5,
        cost=100.0,
        description="Fertilizer",
        date=date(2023, 5, 10),
    ),
    Expense(
        variety="Fuerte",
        quantity=15.0,
        cost=150.0,
        description="Pesticide",
        date=date(2023, 6, 5),
    ),
    Expense(
        variety="Bacon",
        quantity=12.5,
        cost=120.0,
        description="Labor",
        date=date(2023, 7, 1),
    ),
    Expense(
        variety="Zutano",
        quantity=14.0,
        cost=140.0,
        description="Transportation",
        date=date(2023, 7, 15),
    ),
    Expense(
        variety="Reed",
        quantity=11.0,
        cost=110.0,
        description="Tools",
        date=date(2023, 8, 5),
    ),
    Expense(
        variety="Lamb Hass",
        quantity=18.5,
        cost=180.0,
        description="Irrigation",
        date=date(2023, 8, 20),
    ),
    Expense(
        variety="Pinkerton",
        quantity=17.0,
        cost=170.0,
        description="Packaging",
        date=date(2023, 9, 5),
    ),
    Expense(
        variety="Gwen",
        quantity=13.5,
        cost=130.0,
        description="Fertilizer",
        date=date(2023, 9, 15),
    ),
    Expense(
        variety="Sharwil",
        quantity=19.5,
        cost=190.0,
        description="Pesticide",
        date=date(2023, 9, 25),
    ),
    Expense(
        variety="Mexicola",
        quantity=16.0,
        cost=160.0,
        description="Labor",
        date=date(2023, 10, 1),
    ),
]


sales = [
    Sale(buyer_name="John Doe", quantity=12.5, price=125.0, date=date(2023, 5, 15)),
    Sale(buyer_name="Jane Smith", quantity=18.0, price=180.0, date=date(2023, 6, 10)),
    Sale(buyer_name="Tom Hanks", quantity=20.5, price=205.0, date=date(2023, 6, 20)),
    Sale(buyer_name="Emily Blunt", quantity=22.0, price=220.0, date=date(2023, 7, 5)),
    Sale(buyer_name="Chris Evans", quantity=25.0, price=250.0, date=date(2023, 7, 15)),
    Sale(
        buyer_name="Scarlett Johansson",
        quantity=15.5,
        price=155.0,
        date=date(2023, 8, 10),
    ),
    Sale(
        buyer_name="Robert Downey", quantity=17.0, price=170.0, date=date(2023, 8, 20)
    ),
    Sale(buyer_name="Mark Ruffalo", quantity=21.0, price=210.0, date=date(2023, 9, 10)),
    Sale(
        buyer_name="Jeremy Renner", quantity=16.0, price=160.0, date=date(2023, 9, 20)
    ),
    Sale(
        buyer_name="Chadwick Boseman",
        quantity=19.0,
        price=190.0,
        date=date(2023, 10, 1),
    ),
]


distributions = [
    Distribution(
        distributor_name="Distributor A", quantity=100.0, date=date(2023, 5, 20)
    ),
    Distribution(
        distributor_name="Distributor B", quantity=150.0, date=date(2023, 6, 15)
    ),
    Distribution(
        distributor_name="Distributor C", quantity=120.0, date=date(2023, 7, 10)
    ),
    Distribution(
        distributor_name="Distributor D", quantity=180.0, date=date(2023, 8, 5)
    ),
    Distribution(
        distributor_name="Distributor E", quantity=130.0, date=date(2023, 8, 20)
    ),
    Distribution(
        distributor_name="Distributor F", quantity=110.0, date=date(2023, 9, 10)
    ),
    Distribution(
        distributor_name="Distributor G", quantity=160.0, date=date(2023, 9, 25)
    ),
    Distribution(
        distributor_name="Distributor H", quantity=140.0, date=date(2023, 10, 1)
    ),
    Distribution(
        distributor_name="Distributor I", quantity=170.0, date=date(2023, 10, 5)
    ),
    Distribution(
        distributor_name="Distributor J", quantity=190.0, date=date(2023, 10, 10)
    ),
]


session.add_all(varieties)
session.add_all(trees)
session.add_all(irrigations)
session.add_all(harvests)
session.add_all(inventories)
session.add_all(expenses)
session.add_all(sales)
session.add_all(distributions)


session.commit()


session.close()

print("Sample data added successfully!")
