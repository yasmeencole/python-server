ANIMALS = [
    {
        "id": 1,
        "name": "Harry",
        "species": "Pitbull",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1
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