#!/usr/bin/python3
"""
Task 2: C is fun!
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    display "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    display "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """
    display "C " followed by the value
    of the text variable. 
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
