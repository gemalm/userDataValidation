# User Data Validation Testing

This project is designed to validate user data fetched from a REST API endpoint. The primary goal is to ensure that the user data returned from the API complies with expected formats, contains all necessary fields, and maintains consistency across paginated responses.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [Installation](#installation)
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
   
### License
MIT License

Copyright (c) [2024] [Gema López Muñoz]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in
   all copies or substantial portions of the Software.

2. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.