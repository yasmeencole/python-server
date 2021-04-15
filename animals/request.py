import sqlite3
import json
from models import Animal
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
    return ANIMALS

# Function with a single parameter
def get_single_animal(id):
# Variable to hold the found animal, if it exists
    requested_animal = None

# Iterate the ANIMALS list above. Very similar to the
# for..of loops you used in JavaScript.
# this is a for in loop
    for animal in ANIMALS:
    # Dictionaries in Python use [] notation to find a key
    # instead of the dot notation that JavaScript used.
    # this is a if statement
        if animal["id"] == id:
            # sets animal to a new variable
            requested_animal = animal

    return requested_animal

def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal    

def delete_animal(id):
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)    

def update_animal(id, new_animal):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Update the value.
            # animals at the index we are looping through is equal to the new_animal
            ANIMALS[index] = new_animal
            break

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
            a.customer_id
        FROM animal a
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

            animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(animals)        

def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'],
                            data['status'], data['location_id'],
                            data['customer_id'])

        return json.dumps(animal.__dict__)    