#!/usr/bin/python3
"""
Task 9: Cities by states
"""
from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display a HTML page
    all cities of a State
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    closes database
    """
    storage.close()


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
