import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'file.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username and store it."""
    username = input("What is your name? ")
    filename = 'file.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name and verify identity."""
    username = get_stored_username()

    if username:
        correct = input(f"Are you {username}? (y/n): ").strip().lower()
        if correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
