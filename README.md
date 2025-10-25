# hcl_hackthon
Account creation: 
-------------
trigger: customer requests a new account..
flow:
-----
choose account type : 1. savings
                      2. current
                      3. FD account
system generates a 12 digit account number
initial deposit amount.. 
- min 500 to max..
-----------

# Project Overview

This project implements a bank account creation system where:
- Customers can choose between **3 account types**: Savings, Current, or Fixed Deposit (FD)
- The system generates a unique **12-digit account number** automatically
- Customers must provide an **initial deposit** (minimum ₹500)
- The system displays all account details after successful creation

--------

## Features

✅ **Multiple Account Types**
- Savings Account
- Current Account
- Fixed Deposit (FD) Account

✅ **Automated Account Number Generation**
- Unique 12-digit account numbers
- Random generation to ensure uniqueness

✅ **Input Validation**
- Account type selection validation
- Minimum deposit requirement (₹500)
- Numeric input validation for deposits

✅ **Confirmation Display**
- Displays all account details after creation
- Clear user feedback and error messages


- **RESTful API**: All functionality is exposed through a clean and simple API.
- **ORM Integration**: Uses SQLAlchemy to model database tables, providing a clear and maintainable structure.

## Technologies Used

- **Backend**: Python
- **API Framework**: Flask
- **Database ORM**: SQLAlchemy (with Flask-SQLAlchemy)
- **Database**: SQLite (for development)
---
