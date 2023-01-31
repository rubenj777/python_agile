import json
from os import path

menu = "menu.json"
orders = "orders.json"


def add_order(table):

    if path.isfile(orders) is False:
        raise Exception("File not found")

    with open(orders) as fp:
        listOrders = json.load(fp)

    listOrders.append({"Numero de table":table.numero, "Menu":table.menu , "Prix": table.addition})

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


def prog_menu():
    print("Bienvenue dans notre restaurant")
    print("----------------------------------------------------------------------")
    print("1-Menu")
    print("2-prendre une commande")
    print("3-voir la note d'une table")
    print("0-pour quitter")
    print("--------------------------------------------------------------------------")

class Table:
    def _init_(self, numero,addition,menu):
        self.numero=numero
        self.menu=menu
        self.addition=addition


def main():
   prog_menu()
   ma_Table=Table()
   choix =int(input("faites votre choix : "))
   if choix==1:
        see_menu()
   if choix==2:
        print("Prise de commande :")
        print("numero de table :")
        numero_table=input("table numero : ")
        ma_Table.numero=numero_table
        print("quel menu desirez vous")
        monc_choix=input("menu : ")
        ma_Table.menu=monc_choix
        print("entrer l'addition pour cette table ")
        addition=int(input("le montant de l'addition est de : "))
        ma_Table.addition=addition
        add_order(ma_Table)
        print("merci vos commandes ont bien été enregistrées")   
   if choix==3:
        print("on le fera apres")
        
main()