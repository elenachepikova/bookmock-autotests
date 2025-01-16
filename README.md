# Autotests for [BookMock](https://elenachepikova.website3.me/) website

## Description (TO UPDATE)

This project contains a suite of automated tests designed to verify the functionality of
the [BookMock](https://elenachepikova.website3.me/) website.
Additionally, it includes a script for generating and storing random customer data in an SQLite database.

## Technologies (TO REVIEW)

- **Python 3.12**
- **Selenium**: For browser automation
- **pytest**: Testing framework
- **Allure**: For generating test reports
- **SQLIte3**: For test data storage

## Database

The project uses an SQLite database (`customers.db`) to store customer information. The database is automatically
created in the project directory during the execution of the script, if it doesn't already exist.

### Table structure:

- **ID**: Auto-incremented primary key
- **FIRST_NAME**: First name of the customer
- **LAST_NAME**: Last name of the customer
- **EMAIL**: Unique email address of the customer
- **MESSAGE**: Randomly generated message

### How to Run

`customers.db` is automatically created, filled in and used by `customer_db` fixture in corresponding autotests (e.g.
`test_submit_contact_us_form`) No additional actions required to set it up.

## Installation

### Steps

1. Clone the repository:
    ``` bash
        git clone https://github.com/elenachepikova/qap19onl_final_project.git
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
├── core/                           # Directory containing base methods
│   ├── __init__.py                 # Initialization file for the core module
│   ├── actions.py                  # Base page with common methods
│   ├── assertions.py               # Common assertions for test validations
├── data/                           # Directory containing data to be used in tests
│   ├── __init__.py                 # Initialization file for the data module
│   ├── customer_db.py              # Customer DataBase Class (DB generation, fullfillment and usage)
│   └── test_data.py                # Store test data 
├── elements/                       # Directory containing modules related to the locators and interactions with page elements
│   ├── __init__.py                 # Initialization file for the elements module
│   ├── cart.py                     # Element locators and interactions for the shopping cart
│   ├── footer.py                   # Element locators and interactions for the page footer
│   └── header.py                   # Element locators and interactions for the page header (Navigation Panel)
├── pages/                          # Page Object Model (POM) classes
│   ├── __init__.py                 # Initialization file for the pages module
│   ├── about_page.py               # Page object for the About page
│   ├── contact_page.py             # Page object for the Contact page
│   ├── faq_page.py                 # Page object for the FAQ page
│   ├── form_submitted_page.py      # Page object for the form submission success page
│   ├── home_page.py                # Page object for the Home page
│   └── shop_page.py                # Page object for the Shop page
├── tests/                          # Directory containing all test cases
│   ├── test_about.py               # Tests for the about page
│   ├── test_cart.py                # Tests for the cart feature
│   ├── test_contact.py             # Tests for the contact page
│   ├── test_homepage.py            # Tests for the homepage
│   ├── test_navigation_panel.py    # Tests for the navigation panel feature
│   └── test_shop.py                # Tests for the shop feature
├── .gitignore                      # Git ignore file
├── conftest.py                     # pytest configurations and fixtures
├── README.md                       # Project documentation
└──  requirements.txt               # Python dependencies
```

## Author

Author: Elena Chepikova  
GitHub: [github.com/elenachepikova](https://github.com/elenachepikova)