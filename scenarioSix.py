import requests
import re
import pytest


def fetch_users():
    response = requests.get("https://reqres.in/api/users")
    response.raise_for_status()  # Checks for HTTP errors
    return response.json()


def fetch_user_details(user_id):
    response = requests.get(f"https://reqres.in/api/users/{user_id}")
    response.raise_for_status()  # Checks for HTTP errors
    return response.json()


def validate_user_data(user_list, user_details):
    user_data = user_details['data']

    # Validate the user against the user_list
    for user in user_list['data']:
        if user['id'] == user_data['id']:
            assert user['email'] == user_data['email'], "Emails do not match!"
            assert user['first_name'] == user_data['first_name'], "First names do not match!"
            assert user['last_name'] == user_data['last_name'], "Last names do not match!"
            assert user['avatar'] == user_data['avatar'], "Avatars do not match!"
            # Email format validation
            assert re.match(r"[^@]+@[^@]+\.[^@]+", user_data['email']), "Invalid email format!"
            print(f"User {user['id']} validation successful.")
            return
    assert False, f"No user found with ID {user_data['id']}."


def test_validate_multiple_users():
    user_list = fetch_users()
    user_ids = [user['id'] for user in user_list['data']]  # Extracting user IDs from the user list

    for user_id in user_ids:
        user_details = fetch_user_details(user_id)
        validate_user_data(user_list, user_details)


if __name__ == "__main__":
    pytest.main()
