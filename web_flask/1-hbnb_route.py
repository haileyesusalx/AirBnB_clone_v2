#!/usr/bin/python3
"""Start flask web application"""

from flask import Flask

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


if __name__ == "__main__":
    # Start the flask development server
    # Listen on all available network interfces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000) 
