import requests

url = 'https://alu-intranet.hbtn.io/status'

response = requests.get(url)

print('Body response:')
print('\t- type:', type(response.text))
print('\t- content:', response.text)