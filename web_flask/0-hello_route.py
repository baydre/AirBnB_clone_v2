#!/usr/bin/python3
"""
Task 0: Hello Flask!
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """
    display "Hello HBNB!"
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
