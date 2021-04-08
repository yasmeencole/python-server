CUSTOMERS = [
    {
        "id": 1,
        "name": "Mary",
        "locationId": 1,
    },
    {
        "id": 2,
        "name": "Eve",
        "locationId": 1,
    },
    {
        "id": 3,
        "name": "Grey",
        "locationId": 2,
    }
]

# This function is used to look up a single customer, 
# The id of the customer has to be passed as an argument.
# It iterates the entire list with a for..in loop. 
# For each customer, it checks if its id property is the same
# as the id that was passed into the function as a parameter.
# Finally, it returns the value of requested_customer

# function that gets list of customers, does not contain self
def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
# Variable to hold the found customer, if it exists
    requested_customer = None

# Iterate the CUSTOMERS list above. Very similar to the
# for..of loops you used in JavaScript.
# this is a for in loop
    for customer in CUSTOMERS:
    # Dictionaries in Python use [] notation to find a key
    # instead of the dot notation that JavaScript used.
    # this is a if statement
        if customer["id"] == id:
            # sets customer to a new variable
            requested_customer = customer

    return requested_customer