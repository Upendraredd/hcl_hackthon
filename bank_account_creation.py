import mysql.connector
from mysql.connector import Error
import random
from datetime import datetime
import sys

# --- Database Connection using mysql.connector ---
print("Attempting to connect to MySQL database...")

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="Upendr@143",
        database="bank_db", # Added the specific database
        connection_timeout=5
    )

    if connection.is_connected():
        print("Connection to MySQL DB successful")

except Error as e:
    print(f"Error connecting to MySQL: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)

# --- Helper Functions ---
def generate_unique_account_number(cursor):
    """Generates a unique 12-digit account number that doesn't already exist."""
    while True:
        account_number = str(random.randint(10**11, (10**12) - 1))
        cursor.execute("SELECT account_number FROM accounts WHERE account_number = %s", (account_number,))
        if cursor.fetchone() is None:
            return account_number

def display_account_details(account_dict):
    """Prints the details of an account dictionary."""
    print("\n--- Account Details ---")
    print(f"  Name: {account_dict['name']}")
    print(f"  Account Number: {account_dict['account_number']}")
    print(f"  Account Type: {account_dict['account_type']}")
    print(f"  Balance: ₹{account_dict['balance']:.2f}")
    print(f"  PAN: {account_dict['pan_number']}")
    print(f"  Aadhaar: {account_dict['aadhaar_number']}")
    created_on = account_dict['created_at']
    if isinstance(created_on, datetime):
        print(f"  Created On: {created_on.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(f"  Created On: {created_on}")
    print("-----------------------\n")

# --- Main Application Logic ---
def main():
    """Main function to run the bank account CLI."""
    cursor = connection.cursor(dictionary=True) # Use a dictionary cursor

    # Create the table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        pan_number VARCHAR(10) NOT NULL UNIQUE,
        aadhaar_number VARCHAR(12) NOT NULL UNIQUE,
        account_number VARCHAR(12) NOT NULL UNIQUE,
        account_type VARCHAR(50) NOT NULL,
        balance FLOAT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
    )
    connection.commit()

    print("--- Bank Account Management System ---")
    
    # 1. Collect and validate personal data
    name = input("Enter your full name: ")

    while True:
        pan_number = input("Enter your 10-digit PAN number: ").strip().upper()
        if len(pan_number) == 10 and pan_number.isalnum():
            break
        else:
            print("Invalid format. Please enter a 10-character alphanumeric PAN number.")

    while True:
        aadhaar_number = input("Enter your 12-digit Aadhaar number: ").strip()
        if len(aadhaar_number) == 12 and aadhaar_number.isdigit():
            break
        else:
            print("Invalid format. Please enter a 12-digit numeric Aadhaar number.")

    # 2. Check if account already exists
    query = "SELECT * FROM accounts WHERE pan_number = %s OR aadhaar_number = %s"
    cursor.execute(query, (pan_number, aadhaar_number))
    existing_account = cursor.fetchone()

    if existing_account:
        print("\nAn account with these details already exists.")
        display_account_details(existing_account)
        return

    # 3. If not, create a new account
    print("\nNo existing account found. Let's create a new one.")
    
    # Choose account type
    print("Select account type:")
    print("  1. Savings")
    print("  2. Current")
    print("  3. FD Account")
    
    choice = ""
    account_type_map = {"1": "Savings", "2": "Current", "3": "FD"}
    while choice not in account_type_map:
        choice = input("Enter your choice (1/2/3): ")
    account_type = account_type_map[choice]

    # Get initial deposit
    initial_deposit = 0
    while True:
        try:
            deposit_str = input("Enter the initial deposit amount (minimum ₹500): ")
            initial_deposit = float(deposit_str)
            if initial_deposit >= 500:
                break
            else:
                print("Initial deposit must be at least ₹500.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Create the new account
    account_number = generate_unique_account_number(cursor)
    insert_query = """
    INSERT INTO accounts (name, pan_number, aadhaar_number, account_number, account_type, balance)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    new_account_data = (
        name, pan_number, aadhaar_number, account_number, 
        account_type, initial_deposit
    )
    
    cursor.execute(insert_query, new_account_data)
    connection.commit()

    print("\nAccount successfully created!")
    # Fetch the newly created account to display details
    cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (account_number,))
    newly_created_account = cursor.fetchone()
    display_account_details(newly_created_account)


if __name__ == "__main__":
    main()
    # Clean up the connection
    if connection.is_connected():
        connection.close()
        print("\nMySQL connection is closed.")
