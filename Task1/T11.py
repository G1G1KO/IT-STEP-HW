#Task 11


import os
import json

''' 1)
def get_path(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return os.path.abspath(file.name)
    
filename = get_path("T11.txt")
print(filename)
'''





''' 2)
def read_json_file(filename: str) -> list[dict]:
  with open(filename, mode='r', encoding='utf-8') as file:
    return json.load(file)
  

data = read_json_file("files/jsons/del.json")
print(data)
'''








''' 3)
new_players = [
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]


def add_users(filename, new_data: dict):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    id_exists = False
    for player in data:
        if player["id"] == new_data["id"]:
            id_exists = True
            break 

    if id_exists:
        print(f"Error: User with ID {new_data['id']} ({new_data['name']}) already exists!")
        return

    data.append(new_data)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print(f"User {new_data['name']} successfully added!")


filename = "files/jsons/del.json"

for player_dict in new_players:
    add_users(filename, player_dict)
'''


''' 4)
def update_user(filename, player_id, key_to_update: str, new_value):

    with open(filename, "r", encoding="utf-8") as file:
        data_list = json.load(file)

    player_found = False
    for player in data_list:
        if player["id"] == player_id:
            player[key_to_update] = new_value
            player_found = True
            break

    if not player_found:
        print("Wrong ID, Try Again!")
        return
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data_list, file, indent=2, ensure_ascii= False)
        print("Updated Successfully")

filename = "files/jsons/del.json"

update_user(filename, 19, "age", 20)
'''