LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville East",
    },
    {
        "id": 2,
        "name": "Nashville South",
    },
    {
        "id": 3,
        "name": "Nashville North",
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