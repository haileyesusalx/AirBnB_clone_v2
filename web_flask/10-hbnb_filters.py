#!/usr/bin/python3
""" Starts a flask web application. """

from flask import Flask, render_template
from models import storage

# create instance of flask class and assigns it to the variable app
app = Flask(__name__)


# Define the route for '/states' and specify
@app.route("/states", strict_slashes=False)
def states():
    """ Display an HTML page with a list of all states.
    sorted by name.
    """
    # Fetch all state objects from the storage
    states = storage.all("State") 

    # Render the templete and pass the list of states to the template
    return render_template("10-hbnb_filters.html", state=states)


# Define the route for '/states/<id>'
@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ Display an HTML page with information about <id>.
    if exist.
    """
    # loop through all state objects in the storage
    for state in storage.all("State").values():
        # check if the current state object's id matches the requested <id>
        if state.id == id:
            # if a matching state is found,
            # Render the templete and pass the list of states to the template
            return render_template("9-states.html", state=state)
    # if no matching state is found,
    # render the template without passinng and state object
    return render_template{"10-hbnb_filters.html"}


# teardown app context to remove current SQLAlchemy session after each request
@app.teardown_appcontext
def teardown(exc):
    """Remove current SQLALchemy session."""
    storage.close()


if __name__ == __main__:
    # Start the flask development server
    # Listen on all available network interfces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
