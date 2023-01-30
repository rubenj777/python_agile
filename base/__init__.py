import json
from os import path

menu = "menu.json"
orders = "orders.json"


def add_order():

    if path.isfile(orders) is False:
        raise Exception("File not found")

    with open(orders) as fp:
        listOrders = json.load(fp)

    listOrders.append({"Menu": "menu 4", "Prix": 33})

    # Verify updated list
    print(listOrders)

    with open(orders, "w") as json_file:
        json.dump(listOrders, json_file, indent=4, separators=(",", ": "))


def see_menu():

    if path.isfile(menu) is False:
        raise Exception("File not found")

    # Read JSON file
    with open(menu) as fp:
        listObj = json.load(fp)

    # Verify existing list
    print(listObj)


# see_menu()
add_order()