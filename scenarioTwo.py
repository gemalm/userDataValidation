import pytest
import requests

# The URL of the API endpoint we want to test
URL = "https://reqres.in/api/users/2"


def test_get_user_details():
    # Send a GET request to the specified endpoint
    response = requests.get(URL)

    # Assert the status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Parse the response JSON
    json_response = response.json()

    # Validate the expected fields in the response
    expected_user_fields = {"id", "email", "first_name", "last_name", "avatar"}
    expected_support_fields = {"url", "text"}

    # Check the presence of 'data' and 'support' fields
    assert "data" in json_response, "'data' should be present in the response"
    assert "support" in json_response, "'support' should be present in the response"

    user_data = json_response["data"]
    support_info = json_response["support"]

    # Check if all expected fields are present in the user data
    assert expected_user_fields.issubset(
        user_data.keys()), f"Response user JSON keys should include {expected_user_fields}"
    assert expected_support_fields.issubset(
        support_info.keys()), f"Response support JSON keys should include {expected_support_fields}"

    # Validate type of attributes for user data
    assert isinstance(user_data["id"], int), "ID should be an integer"
    assert isinstance(user_data["email"], str), "Email should be a string"
    assert isinstance(user_data["first_name"], str), "First name should be a string"
    assert isinstance(user_data["last_name"], str), "Last name should be a string"
    assert isinstance(user_data["avatar"], str), "Avatar should be a string"

    # Validate specific content
    assert user_data["id"] == 2, "User ID should be 2"
    assert '@' in user_data["email"], "Email should contain '@'"
    assert user_data["first_name"].isalpha(), "First name should contain only alphabetic characters"
    assert user_data["last_name"].isalpha(), "Last name should contain only alphabetic characters"
    assert json_response["support"]["url"].startswith("https://"), "Support URL should start with 'https://'"

    # Validate support information
    assert isinstance(support_info["url"], str), "Support URL should be a string"
    assert isinstance(support_info["text"], str), "Support text should be a string"

    print("All validations passed successfully!")

# If you want to run these tests directly using pytest without specifying the filename, use this:
if __name__ == "__main__":
    pytest.main()