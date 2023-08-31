"""
A simple Flask web application to display "Hello HBNB!", custom messages, and Python messages.
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

@app.route("/c/<text>", strict_slashes=False)
def display_c_text(text):
    """
    Display "C" followed by the value of the text variable.

    Args:
        text (str): The text variable from the URL.

    Returns:
        str: The message "C " followed by the value of text.
    """
    # Replace underscores with spaces
    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"

@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def display_python_text(text):
    """
    Display "Python" followed by the value of the text variable.

    Args:
        text (str): The text variable from the URL.

    Returns:
        str: The message "Python " followed by the value of text.
    """
    # Replace underscores with spaces
    formatted_text = text.replace("_", " ")
    return f"Python {formatted_text}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)