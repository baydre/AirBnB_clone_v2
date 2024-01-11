#!/usr/bin/python3
"""
Task 11: HBNB filters
"""
from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    display a HTML page
    like 6-index in AirBnB clone - Web static.
    """
    amenities = storage.all(Amenity).values()
    states = storage.all(State).values()
    return render_template('10-hbnb_filters.html', states=states,
            amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """
    closes database
    """
    storage.close()


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
