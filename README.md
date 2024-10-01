# User Data Validation Testing

This project is designed to validate user data fetched from a REST API endpoint. The primary goal is to ensure that the user data returned from the API complies with expected formats, contains all necessary fields, and maintains consistency across paginated responses.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Run Tests](#run-tests)
- [Contributing](#contributing)
- [License](#license)
  
## Features

- Fetch user data from a paginated API.
- Validate fields including `id`, `email`, `first_name`, `last_name`, and `avatar`.
- Ensure all fields contain valid, non-empty values.
- Check for duplicates across paginated responses.
- Validate email formats using regex.
- Ensure the total number of users per page matches the expected `per_page` value.

## Getting Started

Follow the instructions below to get a copy of the project up and running on your local machine for development and testing purposes.

### Requirements

- `requests` library for HTTP requests
- `pytest` for running tests

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/user-data-validation.git