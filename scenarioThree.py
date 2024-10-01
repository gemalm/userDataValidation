import pytest
import requests

# API endpoint url for creating a user
URL = "https://reqres.in/api/users"


def test_create_user_valid():
    """Test valid user creation"""
    payload = {
        "name": "John",
        "job": "developer"
    }
    response = requests.post(URL, json = payload)
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    json_response = response.json()
    print(json_response)
    assert json_response["name"] == "John", "The response name should be 'John'"
    assert json_response["job"] == "developer", "The response job should be 'developer'"


def test_create_user_missing_name():
    """Test user creation missing name"""
    payload = {
        "job": "developer"
    }
    response = requests.post(URL, json = payload)
    print(response.status_code)
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    json_response = response.json()
    assert "name" in json_response["error"], "Error message should indicate 'name' is required"

    # Result: The request succeeded, and a new resource was created as a result what it is not the correct functionality.


def test_create_user_missing_job():
    """Test user creation missing job"""
    payload = {
        "name": "John"
    }
    response = requests.post(URL, json = payload)
    print(response.status_code)
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    json_response = response.json()
    assert "job" in json_response["error"], "Error message should indicate 'job' is required"

    # Result: The request succeeded, and a new resource was created as a result what it is not the correct functionality.


def test_create_user_empty_fields():
    """Test user creation with empty fields"""
    payload = {
        "name": "",
        "job": ""
    }
    response = requests.post(URL, json = payload)
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    json_response = response.json()
    print(json_response)
    assert "name" in json_response["error"], "Error message should indicate 'name' is required"
    assert "job" in json_response["error"], "Error message should indicate 'job' is required"

    # Result: The request succeeded, and a new resource was created as a result what it is not the correct functionality.


def test_create_user_no_fields():
    """Test user creation with no fields"""
    payload = {}
    response = requests.post(URL, json = payload)
    print(response.status_code)
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    json_response = response.json()
    assert "name" in json_response["error"], "Error message should indicate 'name' is required"
    assert "job" in json_response["error"], "Error message should indicate 'job' is required"

    # Result: The request succeeded, and a new resource was created as a result what it is not the correct functionality.

# If you want to run these tests directly using pytest without specifying the filename, use this:
if __name__ == "__main__":
    pytest.main()