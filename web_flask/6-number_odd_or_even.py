#!/usr/bin/python3
"""Start flask web application
"""

from flask import Flask, request

app = Flask(__name__)


# Define the route for the root URL (/)
@app.route('/', strict_slashes=False)
def hello_school():
    """ Display 'Hello HBNB!'. """
    return "Hello HBNB!"


# Define the route for the root URL (/hbnb)
@app.route('/hbnb', strict_slashes=False)
def school():
    """ Display 'HBNB'. """
    return "HBNB"


# Define the route for (/c/<text>)
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """ Displays 'C' followed by the value of <text>. """
    # Replace _ with ' ' in text variable
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


# Define the route for (/python/<text>)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """ Displays 'python' followed by the value of <text>. """
    # Replace _ with ' ' in text variable
    formatted_text = text.replace('_', ' ')
    return "Python {}".format(formatted_text)


# Define the route for (/number_odd_or_even/<n>)
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Displays HTML page if only n is an integer.
    States is n odd or even on the body.
    """

    # check n is integer
    if isinstance(n, int):
        # n is even or odd
        even_or_odd = "even" if n % 2 == 0 else "odd"
        # Render the template and pass value
        return render_template('6-number_odd_or_even.html',
                               n=n, even_or_odd=even_or_odd)
    else:
        # if n is not an integer, return error message
        return "Invalid input. please provide an integer."


# Define the route for (/number/<n>)
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Displays 'n is a number' if only n is an integer. """
    return "{} is a number".format(n)


# Define the route for (/number_template/<n>)
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Displays an HTML pag if only n is an integer."""
    # Render the template and pass the value of n to the template
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    # Start the flask development server
    # Listen on all available network interfces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
