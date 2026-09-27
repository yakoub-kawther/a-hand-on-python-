import json

filename = 'file.json'

# Load existing data or start empty
try:
    with open(filename, 'r') as f:
        data = json.load(f)  # Expecting a dictionary
except FileNotFoundError:
    data = {}

name = input("Name? ")

if name in data:
    print(f"Welcome back, {name}! Your favorite number is {data[name]}.")
else:
    number = input("Favorite number? ")
    data[name] = number
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Welcome {name}, we'll remember you!")
