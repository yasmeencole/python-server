import sqlite3
import json
from models import Employee

EMPLOYEES = [
    {
        "id": 1,
        "name": "Kasey",
        "address": "35498 Madison Ave",
        "location_id": 1,
    },
    {
        "id": 2,
        "name": "Ebony",
        "address": "100 Main St",
        "location_id": 1,
    },
    {
        "id": 3,
        "name": "Tia",
        "address": "404 Unknown Ct",
        "location_id": 2,
    }
]


def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
# Variable to hold the found employee, if it exists
    requested_employee = None

# Iterate the EMPLOYEES list above. Very similar to the
# for..of loops you used in JavaScript.
# this is a for in loop
    for employee in EMPLOYEES:
    # Dictionaries in Python use [] notation to find a key
    # instead of the dot notation that JavaScript used.
    # this is a if statement
        if employee["id"] == id:
            # sets employee to a new variable
            requested_employee = employee

    return requested_employee
    
def create_employee(employee):
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee     

def delete_employee(id):
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the EMPLOYEES list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)    

def update_employee(id, new_employee):
    # Iterate the EMPLOYEES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break        

def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
            
        FROM employee e
        """)

        # Initialize an empty list to hold all employee representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an employee instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Employee class above.
            employee = Employee(row['id'], row['name'], row['address'],
                            row['location_id'])

            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)        

def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
            
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'], data['address'],
                            data['location_id'])

        return json.dumps(employee.__dict__)            