import json
from os import path

filename = "data.json"
list = []

def see_menu():

    if path.isfile(filename) is False:
        raise Exception("File not found")
 
    # Read JSON file
    with open(filename) as fp:
        listObj = json.load(fp)
 
    # Verify existing list
    print(listObj)
    print(type(listObj))
 
    listObj.append({
    "Menu": "menu 4",
    "Prix": 33
    })
 
    # Verify updated list
    print(listObj)
 
    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, 
                        indent=4,  
                        separators=(',',': '))
 
    print('Successfully appended to the JSON file')

see_menu()