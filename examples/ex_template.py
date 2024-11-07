# Usage
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from unicore import unicore  # Now you can import uscore as usual



# Allows embedding expressions within a template string, evaluating within a context.

template = "Name: <%= name %>, Age: <%= age %>"
context = {"name": "Alice", "age": 25}
result = unicore.template(template, context)
print(result)  # Output: "Name: Alice, Age: 25"


tmpl = """Name: <% if prefix: %><%= prefix %>. <% endif %><%= name %>
Last Name: <%= lname.upper() %>
<% if email: %>
E-mail: <%= email %>
<% endif %>"""

people = [
    {
        "prefix": "",
        "name": "John",
        "lname": "Doe",
        "email": "johndoe@example.com"
    },
    {
        "prefix": "Mr",
        "name": "James",
        "lname": "Brown",
        "email": "james@brown.net"
    }
]

for person in people:
    result = unicore.template(tmpl, person)
    print(result)
    print('---')