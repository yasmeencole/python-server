import sqlite3
import json
from models import Location
# The sqlite3 package is built into Python and will allow you to query your database. 
# The json package is also built into Python and allows you to serialize Python data structures 
# to JSON format, and vice versa.
# Import Location class so that you can create instances of it for each row of data that gets returned
#  from the database.

# To query the database for all locations, convert each row into an Location instance, convert 
# the list to JSON, and respond to the client request.

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville East",
        "address": "35498 Madison Ave"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "101 Penn Ave"
    },
    {
        "id": 3,
        "name": "Nashville North",
        "address": "64 Washington Heights"
    }
]

# This function is used to look up a single location, 
# The id of the location has to be passed as an argument.
# It iterates the entire list with a for..in loop. 
# For each location, it checks if its id property is the same
# as the id that was passed into the function as a parameter.
# Finally, it returns the value of requested_location

def get_all_locations():
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
# Variable to hold the found location, if it exists
    requested_location = None

# Iterate the LOCATIONS list above. Very similar to the
# for..of loops you used in JavaScript.
# this is a for in loop
    for location in LOCATIONS:
    # Dictionaries in Python use [] notation to find a key
    # instead of the dot notation that JavaScript used.
    # this is a if statement
        if location["id"] == id:
            # sets location to a new variable
            requested_location = location

    return requested_location

def create_location(location):
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    location["id"] = new_id

    # Add the location dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location        

def delete_location(id):
    # Initial -1 value for location index, in case one isn't found
    location_index = -1

    # Iterate the LOCATIONS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Store the current index.
            location_index = index

    # If the location was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)        

def update_location(id, new_location):
    # Iterate the LOCATIONS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Update the value.
            LOCATIONS[index] = new_location
            break        

def get_all_locations():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address

        FROM location l
        """)

        # Initialize an empty list to hold all location representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an location instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Location class above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(locations)        

def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address,

        FROM location l
        WHERE l.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an location instance from the current row
        location = Location(data['id'], data['name'], data['address'])

        return json.dumps(location.__dict__)            