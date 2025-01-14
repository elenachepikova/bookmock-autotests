import random
import sqlite3


def count_rows_in_db():
    """Calculate the actual number of rows in customer.db database"""
    db = sqlite3.connect('customers.db')
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM customers")
    rows_num = cursor.fetchone()[0]

    db.close()

    return rows_num


def get_customer_from_db():
    """Retrieve a random customer data from customer.db based on the current size of customers.db database"""
    rows_num = count_rows_in_db()
    customer_id = random.randint(1, rows_num)

    db = sqlite3.connect('customers.db')
    cursor = db.cursor()

    cursor.execute(f"SELECT first_name, last_name, email, message FROM customers WHERE id = {customer_id}")
    customer_data = cursor.fetchone()

    return customer_data

print(get_customer_from_db())
