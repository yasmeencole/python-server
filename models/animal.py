# this a blueprint to set up how a Animal should look
# allow us to determine how the data should be set up 
# helps us not corrupt our database with incorrect data 

class Animal():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, breed, status, location_id, customer_id):
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id

new_animal = Animal(1, "Harry", "Pitbull", "Admitted", 1, 4)

# print(new_animal)
