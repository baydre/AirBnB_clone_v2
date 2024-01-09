#!/usr/bin/python3
"""
Task 8: List of states.
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    display a HTML page
    with list of all states.
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    closes database
    """
    storage.close()


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
