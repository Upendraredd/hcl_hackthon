# Simple CLI Bank Account System
How i developed
--------------

This is a command-line interface (CLI) application for managing a simple bank account system. It is written in pure Python and connects directly to a MySQL database to perform its operations.

The application allows users to create a new bank account or view details of an existing one based on their personal identification numbers.

## Features

- **Interactive Command-Line Interface**: Guides the user through the process with prompts.
- **Direct Database Interaction**: Uses the `mysql-connector-python` library to execute raw SQL queries against a MySQL database.
- **User Validation**: Checks if a user already exists based on PAN or Aadhaar number.
- **Account Creation**: If the user is new, it allows them to create one of three account types (Savings, Current, FD) with a minimum initial deposit.
- **View Existing Account**: If the user already has an account, it fetches and displays their account details.
- **Automatic Table Creation**: The required `accounts` table is created automatically if it does not exist in the database.

---

## Requirements

- Python 3.x
- A running MySQL server instance.
- The `mysql-connector-python` library.

---

## Setup and Configuration

Follow these steps to set up and run the application.

### 1. Database Setup

You must have a MySQL database created before running the script.

1.  Log into your MySQL server.
2.  Run the following SQL command to create the database:
    ```sql
    CREATE DATABASE bank_db;
    ```

### 2. Application Setup

1.  **Install the required library**:
    Open your terminal or command prompt and install the `mysql-connector-python` package using pip.
    ```sh
    pip install mysql-connector-python
    ```

2.  **Configure the Database Connection**:
    Open the `bank_account_creation.py` file and locate the database connection block. You **must** update the `password` with your own MySQL root password.

    ```python
    # --- Database Connection using mysql.connector ---
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="Your_Password_Here", # <-- UPDATE THIS VALUE
            database="bank_db",
            connection_timeout=5
        )
    ```

---

## How to Run

Once the setup is complete, you can run the application with a single command:

```sh
python bank_account_creation.py
```

The script will start, connect to the database, and prompt you for your details.

## Usage Flow

1.  When you run the script, it will first attempt to connect to the MySQL database.
2.  You will be prompted to enter your full name, 10-digit PAN number, and 12-digit Aadhaar number.
3.  The script will query the database to check if an account with your PAN or Aadhaar already exists.
    - If an account is found, its details will be displayed on the screen.
    - If no account is found, the script will guide you through the new account creation process, asking for an account type and an initial deposit.
4.  After the operation is complete, the connection to the database will be closed.
