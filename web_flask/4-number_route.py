#!/usr/bin/python3
"""
Task 4: Is it a number?
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """
    display "Hello HBNB"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    display "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    display "C ", followed by the value
    of the text variable.
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """
    display "Python ",followed by the value
    of the text variable.
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    display "n is a number"
    only if n is a integer.
    """
    return f"{n:d} is a number"


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
