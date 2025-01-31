import random
import sqlite3


class CustomerDB:
    def __init__(self):
        self.db_path = "./customers.db"
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_path)

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def count_rows_in_db(self):
        """Calculate the actual number of rows in customer.db database"""
        self.connect()
        cursor = self.connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM customers")
        rows_num = cursor.fetchone()[0]

        return rows_num

    def get_customer_from_db(self):
        """Retrieve a random customer data from customer.db based on the current size of customers.db database"""
        rows_num = self.count_rows_in_db()
        customer_id = random.randint(1, rows_num)

        self.connect()
        cursor = self.connection.cursor()

        cursor.execute(
            f"SELECT first_name, last_name, email, address, city, country, state, phone "
            f"FROM customers WHERE id = {customer_id}"
        )
        customer_data = cursor.fetchone()

        return customer_data
