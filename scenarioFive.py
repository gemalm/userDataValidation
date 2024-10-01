import requests
import pytest  # Import pytest for testing

# Base URL for the API. Change this to your actual API base URL
API_URL = 'https://reqres.in/api/users'

def test_get_non_existent_user():
    # GET request to /api/users/23 (non-existent user ID)
    response = requests.get(f'{API_URL}/23')  # Send a GET request for a non-existent user
    assert response.status_code == 404  # Verify that the response status code is 404 (Not Found)
    assert response.text == '{}'  # Ensure that the response body is empty. This works but is less flexible
    assert response.json() == {}  # Preferred method

def test_get_user_with_malformed_id():
    # Test 2: Send a GET request with a malformed user ID (non-numeric ID)
    response = requests.get(f'{API_URL}/abc')  # Send a GET request for a malformed user ID
    assert response.status_code == 404  # Verify that the response status code is 404 (Not found)
    # It should have returned 400 (Bad Request) but we are getting 404 instead so we are not getting an appropiate error.

def test_get_existing_user():
    # GET request to /api/users/{id} for an existing user ID
    response = requests.get(f'{API_URL}/10')  # Send a GET request for an existing user (example ID 10)
    assert response.status_code == 200  # Verify that the response status code is 200 (OK)

    data = response.json()  # Parse the response JSON
    assert data['data']['id'] == 10  # Check that the user ID in the response matches the requested ID
    assert 'email' in data['data']  # Ensure the email field exists
    assert 'first_name' in data['data']  # Ensure the first name field exists
    assert 'last_name' in data['data']  # Ensure the last name field exists
    assert 'avatar' in data['data']  # Ensure the avatar field exists

# If you want to run these tests directly using pytest without specifying the filename, use this:
if __name__ == "__main__":
    pytest.main()