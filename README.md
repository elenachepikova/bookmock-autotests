# Autotests for [BookMock](https://elenachepikova.website3.me/) website

## Description (TO UPDATE)

This project contains a suite of automated tests designed to verify the functionality of the [BookMock](https://elenachepikova.website3.me/) website.
Additionally, it includes a script for generating and storing random customer data in an SQLite database.

## Technologies (TO REVIEW)

- **Python 3.12**
- **Selenium**: For browser automation
- **pytest**: Testing framework
- **Allure**: For generating test reports
- **SQLIte3**: For test data storage

## Database
The project uses an SQLite database (`customers.db`) to store customer information. The database is automatically created in the project directory during the execution of the script, if it doesn't already exist.

### Table structure:
- **ID**: Auto-incremented primary key
- **FIRST_NAME**: First name of the customer
- **LAST_NAME**: Last name of the customer
- **EMAIL**: Unique email address of the customer
- **MESSAGE**: Randomly generated message

### How to Run
To execute the script and populate the database with 50 random customers, run the following command:

   ``` bash
        python run.py
   ```
The main() function will:

- Create the SQLite database and table (if not already created).
- Generate 50 random customers.
- Insert them into the database.  

To view the database, you can use any SQLite viewer or run SQL queries directly via Python.

## Installation

### Steps

1. Clone the repository:
    ``` bash
        git clone https://github.com/elenachepikova/bookmock-autotests.git
        cd bookmock-autotests
    ```   
2. Create a virtual environment:
    ``` bash
        python -m venv venv
        source venv/bin/activate  # For Linux/MacOS
        venv\Scripts\activate  # For Windows
   ```
3. Install the dependencies:
    ``` bash
        pip install -r requirements.txt
   ```
4. Run run.py file in order to create and populate customers database:
   ``` bash
        python run.py
   ```

## Running Tests

### Execute All Tests

``` bash
    python -m pytest
   ```

### Generate Allure Report

1. Run Tests with Allure Results:
    ``` bash
    python -m pytest --alluredir allure-results
    ```
2. Generate Allure Report:
    ``` bash
    allure serve allure-results
    ```

## Project Structure (TO UPDATE)

``` vbnet
├── tests/                # Directory containing all test cases
│   ├── test_login.py     # Tests for the login functionality
│   ├── test_search.py    # Tests for the search feature
│   └── test_checkout.py  # Tests for the checkout process
├── pages/                # Page Object Model (POM) classes
│   ├── base_page.py      # Base page with common methods
│   ├── login_page.py     # Page object for the login page
│   └── search_page.py    # Page object for the search page
├── conftest.py           # pytest configurations and fixtures
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore file
```

## Author

Author: Elena Chepikova  
GitHub: [github.com/elenachepikova](https://github.com/elenachepikova)