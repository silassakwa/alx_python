#!/usr/bin/env python3
"""
This script takes a letter as an argument, sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter, and processes the response.
"""

import requests
import sys

# Check if a letter argument was provided
if len(sys.argv) == 2:
    letter = sys.argv[1]
else:
    letter = ""

# URL for sending the POST request
url = 'http://0.0.0.0:5000/search_user'
# Data to be sent in the POST request
data = {'q': letter}

# Send the POST request
response = requests.post(url, data=data)

try:
    # Try to parse the response as JSON
    json_data = response.json()

    if json_data:
        # Display the id and name from the JSON response
        print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    else:
        # Display a message if the JSON response is empty
        print("No result")

except ValueError:
    # Display an error message if the response is not valid JSON
    print("Not a valid JSON")