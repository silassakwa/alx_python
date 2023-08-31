"""
A simple Flask web application to display "Hello HBNB!".
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    """
    The view function for the home page ("/") of the web application.

    Returns:
        str: The greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    """
    the view function for the hbnb page("/") of web application .
    returns:
    str::hbnb"
    """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)