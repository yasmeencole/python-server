# import statements
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal
from customers import get_all_customers, get_single_customer, create_customer, delete_customer, update_customer
from employees import get_all_employees, get_single_employee, create_employee, delete_employee, update_employee
from locations import get_all_locations, get_single_location, create_location, delete_location, update_location


# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    # self is the first parameter, it is getting passed in automatically for us
    # self is props?
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        # slipts on / string and returns a list
        # path is the route?
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get interger from path parameters at index 2 [2]
        try:
            # Convert the string "2" to the integer 2
            # This is the new parseInt() == int()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

# it is a tuple if the return has a comma in it (resource, id)
        return (resource, id)  # This is a tuple 

    # Here's a class function
    # status is what we passed in the 200 or the 201
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    # setting up functions and something about front end
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        self._set_headers(200)
        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        # this (resource, id), the stuff on the left hand side, is unpacking a tuple
        (resource, id) = self.parse_url(self.path)

        # if self.path == "/animals":
        #     response = get_all_animals()
        # else:
        #     response = []      
        if resource == "animals":
            # if this is true then get a signle animal
            if id is not None:
            # In Python, this is a list of dictionaries
            # In JavaScript, you would call it an array of objects
            # gets a signle animal
                response = f"{get_single_animal(id)}"
            # else, this is false, then it gets back all of the animals
            else:
                response = f"{get_all_animals()}"

        if resource == "employees":
            # if this is true then get a signle employee
            if id is not None:
            # In Python, this is a list of dictionaries
            # In JavaScript, you would call it an array of objects
            # gets a signle employee
                response = f"{get_single_employee(id)}"
            # else, this is false, then it gets back all of the employees
            else:
                response = f"{get_all_employees()}"

        if resource == "locations":
            # if this is true then get a signle location
            if id is not None:
            # In Python, this is a list of dictionaries
            # In JavaScript, you would call it an array of objects
            # gets a signle location
                response = f"{get_single_location(id)}"
            # else, this is false, then it gets back all of the locations
            else:
                response = f"{get_all_locations()}"   

        if resource == "customers":
            # if this is true then get a signle customer
            if id is not None:
            # In Python, this is a list of dictionaries
            # In JavaScript, you would call it an array of objects
            # gets a signle customer
                response = f"{get_single_customer(id)}"
            # else, this is false, then it gets back all of the customers
            else:
                response = f"{get_all_customers()}"                 

        # wfile contains the output stream for writing a response back to the client. Proper adherence to the HTTP protocol
        # must be used when writing to this stream in order to achieve successful interoperation with HTTP clients.
        # sends a response back to the client
        self.wfile.write(response.encode())


    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        # Set response code to 201 'Created'
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        # rfile reads response from server
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        new_object = None

        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resource == "animals":
            new_object  = create_animal(post_body)

        if resource == "customers":
            new_object  = create_customer(post_body) 

        if resource == "employees":
            new_object  = create_employee(post_body)

        if resource == "locations":
            new_object  = create_location(post_body)            
        
        # Encode the new animal and send in response
        self.wfile.write(f"{new_object }".encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.
    # PUT request is used to update resource
    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        # turns into post body when json loads
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # checks for resourse, passes id and post body
        if resource == "animals":
            update_animal(id, post_body)

        if resource == "customers":
            update_customer(id, post_body)    

        if resource == "employees":
            update_employee(id, post_body)  

        if resource == "locations":
            update_location(id, post_body)        

        # Encode the new animal and send in response
        self.wfile.write("".encode())


    def do_DELETE(self):
    # Set a 204 response code
    # A 204 response code in HTTP means, "I, the server, successfully processed your request, 
    # but I have no information to send back to you."
        self._set_headers(204)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

    # Delete a single animal from the list
        if resource == "animals":
            delete_animal(id)

        if resource == "customers":
            delete_customer(id)

        if resource == "employees":
            delete_employee(id)  

        if resource == "locations":
            delete_location(id)  

    # Encode the new animal and send in response
        self.wfile.write("".encode())    


# This function is not inside the class. It is the starting
# point of this application.
def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()

# run pipenv shell to create virtul environment