import json

# Specify the path to the JSON file relative to your current working directory
file_path = 'Database\pokemons_db.json'

# Open the JSON file
with open(file_path) as file:
    data = json.load(file)

# Access the contents of the JSON file


listing = data['pokemons']
#print(listing)

number = 0
for item in listing:
    for x,y in item.items():
        if x == "name" and y == "Bulbasaur":
            print(listing[number])