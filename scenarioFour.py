import pytest
import requests

# Base URL for the API. Change this to your actual API base URL
API_URL = 'https://reqres.in/api/users'


def test_pagination():
    """Validate pagination handling and the integrity of data across pages."""

    # Test that verifies the correct number of users is returned on page 2
    response = requests.get(f'{API_URL}?page=2')  # Send a GET request to page 2
    assert response.status_code == 200  # Check if the response status code is 200 (OK)

    data = response.json()  # Parse the response JSON
    assert len(data['data']) == 6  # Check that 6 users are returned (default per page)

    # Test that validates pagination fields
    assert data['page'] == 2  # Check if the current page number is correct
    assert data['per_page'] == 6  # Check if the number of users per page is correct
    assert 'total' in data  # Ensure the 'total' key exists in the response
    assert 'total_pages' in data  # Ensure the 'total_pages' key exists in the response

    # Test that ensure users are unique in page 1 and page 2
    response_page_1 = requests.get(f'{API_URL}?page=1')  # Fetch users from page 1
    response_page_2 = requests.get(f'{API_URL}?page=2')  # Fetch users from page 2

    data_page_1 = response_page_1.json()  # Parse the response JSON for page 1
    data_page_2 = response_page_2.json()  # Parse the response JSON for page 2

    # Create sets of user IDs for both pages
    users_page_1 = {user['id'] for user in data_page_1['data']}
    users_page_2 = {user['id'] for user in data_page_2['data']}

    # Check that there are no common users between the two pages
    assert users_page_1.isdisjoint(users_page_2)  # Assert that the sets are disjoint (no intersection)

    # Test that attempt to access a non-existent page
    response_non_existent = requests.get(f'{API_URL}?page=999')  # Request a page that doesn't exist
    assert response_non_existent.status_code == 200  # Check the response status code (should still be 200)

    data_non_existent = response_non_existent.json()  # Parse the JSON response
    assert data_non_existent['data'] == []  # Ensure it returns an empty list of users

# If you want to run these tests directly using pytest without specifying the filename, use this:
if __name__ == "__main__":
    pytest.main()