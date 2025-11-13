# 0x03. Unittests and Integration Tests

## Description
This project contains comprehensive unit tests and integration tests for a Python backend application. It demonstrates best practices for testing, including mocking, parameterization, and fixture-based testing.

## Learning Objectives
- Understand the difference between unit tests and integration tests
- Use common testing patterns such as mocking, parametrizations, and fixtures
- Write unit tests for functions and classes
- Write integration tests that test code paths end-to-end

## Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should use the pycodestyle style (version 2.5)
- All files must be executable
- All modules should have documentation
- All classes should have documentation
- All functions should have documentation
- All functions and coroutines must be type-annotated

## Files

### Test Files
- **test_utils.py**: Unit tests for utility functions
  - TestAccessNestedMap: Tests for access_nested_map function
  - TestGetJson: Tests for get_json function with mocked HTTP calls
  - TestMemoize: Tests for memoize decorator

- **test_client.py**: Unit and integration tests for GithubOrgClient
  - TestGithubOrgClient: Unit tests for GithubOrgClient class methods
  - TestIntegrationGithubOrgClient: Integration tests using fixtures

### Source Files
- **utils.py**: Utility functions module
  - `access_nested_map(nested_map, path)`: Access nested map with key path
  - `get_json(url)`: Get JSON from remote URL
  - `memoize`: Decorator to memoize methods

- **client.py**: GitHub organization client module
  - `GithubOrgClient`: Class to interact with GitHub API
    - `org()`: Get organization information
    - `_public_repos_url`: Property to get public repos URL
    - `repos_payload()`: Get repository payload
    - `public_repos(license)`: Get public repositories, optionally filtered by license
    - `has_license(repo, license_key)`: Check if repository has specific license

- **fixtures.py**: Test fixtures for integration tests
  - `ORG_PAYLOAD`: Mock GitHub organization data
  - `REPOS_PAYLOAD`: Mock repository list with license information

## Usage

### Running Tests
```bash
# Run all tests
python3 -m pytest

# Run specific test file
python3 -m pytest test_utils.py
python3 -m pytest test_client.py

# Run with verbose output
python3 -m pytest -v
```

### Running Tests with Coverage
```bash
python3 -m pytest --cov=. --cov-report=html
```

## Tasks Overview

### Task 0: Parameterize a unit test
Create TestAccessNestedMap class with test_access_nested_map method using @parameterized.expand.

### Task 1: Parameterize a unit test (Exception)
Implement TestAccessNestedMap.test_access_nested_map_exception to test exception cases.

### Task 2: Mock HTTP calls
Define TestGetJson class with test_get_json method that uses @patch to mock requests.get.

### Task 3: Parameterize and patch
Implement TestMemoize class with test_memoize method to test the memoize decorator.

### Task 4: Parameterize and patch as decorators
Declare TestGithubOrgClient class and implement test_org method using @patch.

### Task 5: Mocking a property
Implement test_public_repos_url method to test the _public_repos_url property.

### Task 6: More patching
Implement TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos.

### Task 7: Parameterize
Implement TestGithubOrgClient.test_has_license to unit-test GithubOrgClient.has_license.

### Task 8: Integration test: fixtures
Create TestIntegrationGithubOrgClient class with fixtures for integration testing.

## Author
ALX Backend Python Project

## License
This project is part of the ALX Software Engineering Program.
