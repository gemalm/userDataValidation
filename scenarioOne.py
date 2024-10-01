import requests  # Import the requests library for making HTTP requests
import pytest  # Import the pytest library for writing test cases

# Define the URL of the login API endpoint
API_URL = 'https://reqres.in/api/login'


def test_successful_login():
    """Test successful login with valid credentials."""
    # Define the payload (data) for the POST request with valid login credentials
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    # Send a POST request to the API with the valid payload and capture the response
    response = requests.post(API_URL, json = payload)

    # Assert that the response status code is 200 (OK), meaning login was successful
    assert response.status_code == 200

    # Assert that the response JSON contains a 'token' field, indicating successful authentication
    assert 'token' in response.json()  # Validate token existence


def test_missing_password():
    """Test login with only email provided."""
    # Define the payload with only the email (missing password)
    payload = {
        "email": "eve.holt@reqres.in"
    }

    # Send a POST request to the API with the payload containing only the email
    response = requests.post(API_URL, json = payload)

    # Assert that the response status code is 400 (Bad Request) for missing password
    assert response.status_code == 400

    # Assert that the response JSON matches the expected error message for a missing password
    assert response.json() == {"error": "Missing password"}


def test_missing_email():
    """Test login with only password provided."""
    # Define the payload with only the password (missing email)
    payload = {
        "password": "cityslicka"
    }

    # Send a POST request to the API with the payload containing only the password
    response = requests.post(API_URL, json = payload)

    # Assert that the response status code is 400 (Bad Request) for missing email
    assert response.status_code == 400

    # Assert that the response JSON matches the expected error message for a missing email
    assert response.json() == {"error": "Missing email or username"}


def test_content_type_header():
    """Test that the Content-Type header in the response is application/json."""
    response = requests.get(API_URL)

    # Check if the Content-Type header is present and correct
    assert 'Content-Type' in response.headers
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'


def test_empty_request_body():
    """Test sending an empty request body."""
    # Send a POST request to the API with an empty JSON object as the body
    response = requests.post(API_URL, json = {})

    # Assert that the response status code is 400 (Bad Request) for missing required fields
    assert response.status_code == 400

    # Assert that the response JSON matches the expected error message for missing parameters
    assert response.json() == {"error": "Missing email or username"}


# If you want to run these tests directly using pytest without specifying the filename, use this:
if __name__ == "__main__":
    pytest.main()