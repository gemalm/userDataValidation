import requests
import re
import pytest


def fetch_users(page):
    response = requests.get(f"https://reqres.in/api/users?page={page}")
    response.raise_for_status()  # Checks for HTTP errors
    return response.json()


def validate_user_data(user_list):
    for user in user_list:
        # Validate the user
        assert 'id' in user, "User ID is missing!"
        assert 'email' in user, "Email is missing!"
        assert 'first_name' in user, "First name is missing!"
        assert 'last_name' in user, "Last name is missing!"
        assert 'avatar' in user, "Avatar is missing!"

        # Validate each field is non-empty
        assert user['id'] is not None, "ID should not be None!"
        assert user['email'], "Email should not be empty!"
        assert user['first_name'], "First name should not be empty!"
        assert user['last_name'], "Last name should not be empty!"
        assert user['avatar'], "Avatar should not be empty!"

        # Email format validation
        assert re.match(r"[^@]+@[^@]+\.[^@]+", user['email']), "Invalid email format."


def test_validate_users_with_pagination():
    user_ids_page_1 = set()  # Using a set to track unique IDs

    # Fetch and validate users from page 1
    user_list_page_1 = fetch_users(1)
    assert user_list_page_1['per_page'] == len(user_list_page_1['data']), "User count does not match per_page value."
    validate_user_data(user_list_page_1['data'])

    for user in user_list_page_1['data']:
        user_ids_page_1.add(user['id'])

    # Fetch and validate users from page 2
    user_list_page_2 = fetch_users(2)
    assert user_list_page_2['per_page'] == len(user_list_page_2['data']), "User count does not match per_page value."
    validate_user_data(user_list_page_2['data'])

    # Check for duplicates between pages
    user_ids_page_2 = set(user['id'] for user in user_list_page_2['data'])

    # Ensure no duplicates between pages
    assert user_ids_page_1.isdisjoint(user_ids_page_2), "Duplicate user IDs found between page 1 and page 2."


if __name__ == "__main__":
    pytest.main()