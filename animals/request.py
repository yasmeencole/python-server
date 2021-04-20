import sqlite3
import json
from models import Animal, Location, Customer
# The sqlite3 package is built into Python and will allow you to query your database. 
# The json package is also built into Python and allows you to serialize Python data structures 
# to JSON format, and vice versa.
# Import Animal class so that you can create instances of it for each row of data that gets returned
#  from the database.

# To query the database for all animals, convert each row into an Animal instance, convert 
# the list to JSON, and respond to the client request.

ANIMALS = [
    {
        "id": 1,
        "name": "Harry",
        "breed": "Pitbull",
        "status": "Admitted",
        "location_id": 1,
        "customer_id": 4
    },
    {
        "id": 2,
        "name": "Jax",
        "breed": "Beagle",
        "status": "Admitted",
        "location_id": 1,
        "customer_id": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "breed": "Cat",
        "status": "Admitted",
        "location_id": 2,
        "customer_id": 1
    }
]

# This function is used to look up a single animal, 
# The id of the animal has to be passed as an argument.
# It iterates the entire list with a for..in loop. 
# For each animal, it checks if its id property is the same
# as the id that was passed into the function as a parameter.
# Finally, it returns the value of requested_animal

# function that gets list of animals, does not contain self
def get_all_animals():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
        a.id,
        a.name,
        a.breed,
        a.status,
        a.location_id,
        a.customer_id,
        l.name location_name,
        l.address location_address,
        c.name customer_name,
        c.address customer_address
        FROM Animal a
        JOIN Location l
        ON l.id = a.location_id
        JOIN Customer c
        ON c.id = a.customer_id
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # returns everything that matches the query
        # Convert rows of data into a Python list
        # fetchall() returning a easier version of the rows that come back
        # appending animal dictionary to animal list
        # fetchall() fetches all the data
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # The database fields are specified in
            # exact order of the parameters defined in the Animal class.
            # use bracket notation to get the value of the keys, pass in parameters for class
            animal = Animal(row['id'], row['name'], row['breed'], row['status'], row['location_id'], row['customer_id'])
            
            # Create a Location instance from the current row
            location = Location(row['location_id'], row['location_name'], row['location_address'])
            
            # Create a Customer instance from the current row
            customer = Customer(row['customer_id'], row['customer_name'], row['customer_address'])
            # .__dict__ : is a dictionary or other mapping object used to store an object’s (writable) attributes.
            # Add the dictionary representation of the location and customer to the animal
            animal.location = location.__dict__
            animal.customer = customer.__dict__
            # Adds the dictionary representation of the animal to the list
            animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
    # pass dumps a list of dictionaries
    return json.dumps(animals)   

# # Function with a single parameter
# def get_single_animal(id):
# # Variable to hold the found animal, if it exists
#     requested_animal = None

# # Iterate the ANIMALS list above. Very similar to the
# # for..of loops you used in JavaScript.
# # this is a for in loop
#     for animal in ANIMALS:
#     # Dictionaries in Python use [] notation to find a key
#     # instead of the dot notation that JavaScript used.
#     # this is a if statement
#         if animal["id"] == id:
#             # sets animal to a new variable
#             requested_animal = animal

#     return requested_animal

# Function with a single parameter
def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        # tables to grab FROM
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address,
            c.name customer_name,
            c.address customer_address
        FROM Animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
            ON c.id = a.customer_id
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'], data['status'], data['location_id'], data['customer_id'])
        
        # Create a Location instance from the current row
        location = Location(data['location_id'], data['location_name'], data['location_address'])
        
        # Create a Customer instance from the current data
        customer = Customer(data['customer_id'], data['customer_name'], data['customer_address'])
        # .__dict__ : is a dictionary or other mapping object used to store an object’s (writable) attributes.
        # Add the dictionary representation of the location and customer to the animal
        animal.location = location.__dict__
        
        animal.customer = customer.__dict__

    return json.dumps(animal.__dict__)    

# def create_animal(animal):
#     # Get the id value of the last animal in the list
#     max_id = ANIMALS[-1]["id"]

#     # Add 1 to whatever that number is
#     new_id = max_id + 1

#     # Add an `id` property to the animal dictionary
#     animal["id"] = new_id

#     # Add the animal dictionary to the list
#     ANIMALS.append(animal)

#     # Return the dictionary with `id` property added
#     return animal    

def create_animal(new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Animal
            ( name, breed, status, location_id, customer_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_animal['name'], new_animal['breed'], new_animal['status'], new_animal['location_id'], new_animal['customer_id'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        # to find out the last id that was inserted
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        # add the id to new animal
        new_animal['id'] = id
    # return json string of new animal
    return json.dumps(new_animal)

def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))

    # Initial -1 value for animal index, in case one isn't found
    # animal_index = -1

    # # Iterate the ANIMALS list, but use enumerate() so that you
    # # can access the index value of each item
    # for index, animal in enumerate(ANIMALS):
    #     if animal["id"] == id:
    #         # Found the animal. Store the current index.
    #         animal_index = index

    # # If the animal was found, use pop(int) to remove it from list
    # if animal_index >= 0:
    #     ANIMALS.pop(animal_index)    

# def update_animal(id, new_animal):
#     # Iterate the ANIMALS list, but use enumerate() so that
#     # you can access the index value of each item.
#     for index, animal in enumerate(ANIMALS):
#         if animal["id"] == id:
#             # Found the animal. Update the value.
#             # animals at the index we are looping through is equal to the new_animal
#             ANIMALS[index] = new_animal
#             break   

def update_animal(id, new_animal):
    # connection to the database and its path
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        # set up sql that I want to execute
        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (
            # tuple of animal properties that I want to update
            new_animal['name'], new_animal['breed'], new_animal['status'], new_animal['location_id'], new_animal['customer_id'], id, ))
        
        # Were any rows affected? checks to see which rows were updated or returned
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount
    # If there is no animal with that id value, the rows_affected variable will be 0.
    if rows_affected == 0:
        # If the id is 0, then the user specified an id that doesn't exist
        # this will return False which generates a 404 (Not Found) response back to the client.
        # Forces 404 response by main module
        return False
    else:
        # HTTP Status 204 (No Content) indicates that the server has successfully 
        # fulfilled the request and that there is no content to send in the response payload body
        # Forces 204 response by main module
        return True  