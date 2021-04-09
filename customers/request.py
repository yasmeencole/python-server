CUSTOMERS = [
    {
    # this is a dictionary
        "id": 1,
        "name": "Mary",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Eve",
        "locationId": 1
    },
    {
        "id": 3,
        "name": "Grey",
        "locationId": 2
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

def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    # .append() is similiar to .push a js method
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)        