class Location():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name):
        self.id = id
        self.name = name

new_location = Location(1, "Kasey", 1)