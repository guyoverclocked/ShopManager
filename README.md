# Shop Management System

This is a Python-based shop management system that uses MySQL for managing product inventory and employee records.

## Features

- Add new products
- Add new employees
- Update product details
- Update employee details
- Delete products
- Delete employees
- Display product inventory
- Display employee details
- Update stock inventory
- Handle sales and update stock inventory

## Requirements

- Python 3.x
- MySQL database
- `mysql-connector-python` package
- `mailjet_rest` package

## Setup

1. Install the required packages:
   ```sh
   pip install mysql-connector-python mailjet_rest
   ```
2. Set up the MySQL database with the following tables:
    ```sql
    CREATE DATABASE Shop;

    USE Shop;

    CREATE TABLE PRODUCT (
        s_no INT,
        P_no VARCHAR(255) PRIMARY KEY,
        P_type VARCHAR(255),
        P_cost INT,
        invent INT
    );

    CREATE TABLE EMPLOYEE (
        S_no INT,
        emp_no VARCHAR(255) PRIMARY KEY,
        emp_name VARCHAR(255),
        DOJ DATE,
        Dept VARCHAR(255),
        Sal INT
    );
``

3. Update the database connection details in the script (host, user, password, database):

## Usage
Run the script:
```sh
python juice.py
```
Follow the on-screen prompts to manage the shop's inventory and employee records.

## License
This project is licensed under the MIT License.