#!/usr/bin/env python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./6-my_github.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
personal_access_token = sys.argv[2]

url = f'https://api.github.com/user'
headers = {
    'Authorization': f'Basic {username}:{personal_access_token}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    user_id = user_data.get('id')
    print(user_id)
else:
    print(None)
