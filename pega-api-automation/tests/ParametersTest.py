import requests

parameters = {'page': 1, 'per_page': 1}

url = 'https://gorest.co.in/public/v2/users'

response = requests.get(url, params=parameters)
print(response.json())
assert response.status_code == 200
