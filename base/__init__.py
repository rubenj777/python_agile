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

def prog_Menu():
    print("Bienvenue dans notre restaurant")
    print("----------------------------------------------------------------------")
    print("1-Menu")
    print("2-prendre une commande")
    print("3-voir la note d'une table")

def main():
   prog_Menu()
   choix =input("faites votre choix : ")
   if choix==1:
        see_menu()
   if choix==2:
        add_order()
   if choix==3:
        print("on verra la fonction pour la note")
