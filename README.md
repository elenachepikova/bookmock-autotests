# Autotests for [BookMock](https://elenachepikova.website3.me/) website

## Overview

This repository contains a comprehensive suite of automated tests for
the [BookMock](https://elenachepikova.website3.me/) website. The test suite includes:

- **API Tests**: To validate backend functionality
- **Functional Tests**: To ensure key user workflows operate correctly
- **UI Tests**: To verify frontend elements and interactions

Additionally, the project utilizes an SQLite database (`customers.db`) for test data related to the checkout process.

---

## Technologies Used

- **Python 3.12**
- **Selenium**: Web browser automation
- **pytest**: Testing framework
- **Allure Report**: Test reporting and visualization
- **SQLite3**: Test data storage
- **Flake8**: Code quality checks

---

## Database Integration

The project leverages an SQLite database (`customers.db`) to store customer details used in checkout-related tests. The
database is pre-populated with **50 sample customer records**.

### Table Structure:

```
id          INTEGER (Auto-increment)      # Unique identifier
first_name  TEXT                          # Customer's first name
last_name   TEXT                          # Customer's last name
email       TEXT                          # Customer's email
address     TEXT                          # Customer's address
city        TEXT                          # City of residence
country     TEXT                          # Country of residence
state       TEXT                          # State/Region
phone       TEXT                          # Customer's contact number
```

The `customers.db` file is automatically accessed by the `customer_db` fixture in relevant tests (e.g.,
`test_place_order`), requiring no manual setup.

---

## Installation Guide

### Prerequisites:

Ensure you have **Python 3.12** installed.

### Setup Instructions:

1. Clone the repository:
    ```bash
    git clone https://github.com/elenachepikova/qap19onl_final_project.git
    cd bookmock-autotests
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

### Run All Tests

```bash
python -m pytest
```

### Run Tests by Category

```bash
python -m pytest -m api         # API Tests
python -m pytest -m functional  # Functional Tests
python -m pytest -m ui          # UI Tests
python -m pytest -m smoke       # Smoke Tests
python -m pytest -m regression  # Regression Tests
```

### Generating Allure Reports

1. Run tests and generate test results:
    ```bash
    python -m pytest --alluredir allure-results
    ```
2. Generate and serve the report:
    ```bash
    allure serve allure-results
    ```

---

## Project Structure

``` vbnet
├── .github/                        # GitHub workflows (Flake8 > API tests on pull request & push to main)
├── core/                           # Directory containing base methods
├── data/                           # Directory containing data to be used in tests
├── elements/                       # Directory containing modules related to the locators and interactions with page elements
├── pages/                          # Page Object Model (POM) classes
├── services/                       # Services and API interaction layers
├── tests/                          # Directory containing api, functional, and ui tests
├── .gitignore                      # Git ignore file
├── customers.db                    # SQLite test database
├── pytest.ini                      # Pytest configuration
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
└── setup.cfg                       # Configuration file
```

---

## Author

Author: Elena Chepikova  
GitHub: [github.com/elenachepikova](https://github.com/elenachepikova)