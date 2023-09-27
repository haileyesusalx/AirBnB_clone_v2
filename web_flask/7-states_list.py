#!/usr/bin/python3
""" Starts a flask web application. """

from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

# create instance of flask class and assigns it to the variable app
app = Flask(__name__)


# teardown app context to remove current SQLAlchemy session after each request
@app.teardown_appcontext
def teardown(exception):
    """Remove current SQLALchemy session."""
    storage.close()


# Define the route for '/states_list'
@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Display an HTML page with a list of all state objects in DBstorage.
    sorted by name.
    """
    # Fetch all state objects from the DBstorage and sort them by name A to Z
    states = sorted(storage.all(State).values(), key=lambda s: s.name)

    # Render the templete and pass the list of states to the template
    return render_template("7-states_list.html", states=states)


if __name__ == __main__:
    # Start the flask development server
    # Listen on all available network interfces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
