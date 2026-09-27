person = {
    'first_name': 'Aymen',
    'last_name': 'Houche',
    'age': 22,
    'city': 'Oran'
}

print("First name:", person['first_name'])
print("Last name:", person['last_name'])
print("Age:", person['age'])
print("City:", person['city'])

##################
favorite_numbers = {
    'Kawther': 7,
    'Amel': 12,
    'Sami': 3,
    'Zahra': 5,
    'Nassim': 9
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")

###################