from mailjet_rest import Client
import mysql.connector

# Establishing connection to the MySQL database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="Shop"
)
cur = conn.cursor()

def addProduct():
    """Adds a new product to the database."""
    s_no = int(input('Enter serial number: '))
    P_no = input('Enter product number: ')
    P_type = input('Enter product name: ')
    P_cost = int(input('Enter cost: '))
    invent = int(input('Enter currently available stock: '))
    query = "INSERT INTO PRODUCT VALUES({}, '{}', '{}', {}, '{}')".format(s_no, P_no, P_type, P_cost, invent)
    cur.execute(query)
    conn.commit()
    print("\nProduct Inserted\n")

def addEmp():
    """Adds a new employee to the database."""
    S_no = int(input('Enter serial number: '))
    emp_no = input('Enter employee number: ')
    emp_name = input('Enter employee name: ')
    DOJ = input('Enter date of joining: ')
    Dept = input('Enter department: ')
    Sal = int(input('Enter salary of the employee: '))
    query = "INSERT INTO EMPLOYEE VALUES({}, '{}', '{}', '{}', '{}', {})".format(S_no, emp_no, emp_name, DOJ, Dept, Sal)
    cur.execute(query)
    conn.commit()
    print("\nEmployee Inserted\n")

def P_Update():
    """Updates product details in the database."""
    data = input('Enter product number to be updated: ')
    print('Enter new data')
    sno = int(input('Enter serial number: '))
    ptype = input('Enter product name: ')
    cost = int(input('Enter cost: '))
    query = "UPDATE PRODUCT SET s_no='{}', P_type='{}', P_cost='{}' WHERE P_no='{}'".format(sno, ptype, cost, data)
    cur.execute(query)
    conn.commit()
    print("\nProduct Updated\n")

def E_Update():
    """Updates employee details in the database."""
    Data = input('Enter Employee number to be updated: ')
    print('Enter new data')
    Sno = int(input('Enter serial number: '))
    empname = input('Enter employee name: ')
    doj = input('Enter date of joining: ')
    dept = input('Enter department: ')
    sal = int(input('Enter salary of the employee: '))
    query = "UPDATE Employee SET S_no='{}', emp_name='{}', DOJ='{}', Dept='{}', Sal='{}' WHERE emp_no='{}'".format(Sno, empname, doj, dept, sal, Data)
    cur.execute(query)
    conn.commit()
    print("\nEmployee Updated\n")

def P_delete():
    """Deletes a product from the database."""
    no = input('Enter product number to be deleted: ')
    query = "DELETE FROM product WHERE p_no = '{}'".format(no)
    cur.execute(query)
    conn.commit()
    print("\nProduct Deleted\n")

def E_delete():
    """Deletes an employee from the database."""
    no = input('Enter employee number to be deleted: ')
    query = "DELETE FROM employee WHERE emp_no = '{}'".format(no)
    cur.execute(query)
    conn.commit()
    print("\nEmployee Deleted\n")

def sales():
    """Handles sales and updates stock inventory."""
    total = 0
    inventory = 0
    print("Enter -1 to stop shopping")
    while True:
        jk = 0
        prr = input("Enter product number: ")
        if prr == '-1':
            break
        quan = int(input("Enter quantity: "))
        cur.execute(f"select p_cost from product where p_no = '{int(prr)}'")
        for i in cur:
            jk += i[0]
        total += int(jk) * quan
        cur.execute(f"select invent from product where p_no = '{int(prr)}'")
        for k in cur:
            inventory += int(k[0])
        inventory -= quan
        print(inventory)
        cur.execute(f"update product set invent = '{int(inventory)}' where p_no = '{int(prr)}'")
        conn.commit()
        print(f"Your current total is {total}")
        if inventory < 20:
            print("Stock is low. Please refill!")

def display_inventory():
    """Displays the current inventory."""
    cur.execute("select p_type from product")
    prname = [i[0] for i in cur]
    cur.execute("select p_cost from product")
    prcost = [j[0] for j in cur]
    cur.execute("select invent from product")
    inventr = [p[0] for p in cur]
    for k in range(len(prcost)):
        print(prname[k], prcost[k], inventr[k])

def E_display():
    """Displays employee details."""
    cur.execute("SELECT * FROM EMPLOYEE")
    for row in cur.fetchall():
        print(row)

def inv_update():
    """Updates the stock inventory."""
    p_no = input("Enter product number to update inventory: ")
    new_invent = int(input("Enter new stock quantity: "))
    query = "UPDATE product SET invent = {} WHERE p_no = '{}'".format(new_invent, p_no)
    cur.execute(query)
    conn.commit()
    print("\nInventory Updated\n")

while True:
    print('_' * 16)
    print('SHOP MANAGEMENT')
    print('_' * 16)
    print('1. Add new product')
    print('2. Add new employee')
    print('3. Update product')
    print('4. Update employee')
    print('5. Delete product')
    print('6. Delete employee')
    print('7. Display product')
    print('8. Display employee')
    print('9. Update Stocks')
    print('0. Sales')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        addProduct()
    elif choice == 2:
        addEmp()
    elif choice == 3:
        P_Update()
    elif choice == 4:
        E_Update()
    elif choice == 5:
        P_delete()
    elif choice == 6:
        E_delete()
    elif choice == 7:
        display_inventory()
    elif choice == 8:
        E_display()
    elif choice == 9:
        inv_update()
    elif choice == 0:
        sales()
    else:
        print('Invalid choice')
        break
