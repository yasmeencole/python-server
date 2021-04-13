ANIMALS = [
    {
        "id": 1,
        "name": "Harry",
        "species": "Pitbull",
        "status": "Admitted",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "status": "Admitted",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "status": "Admitted",
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