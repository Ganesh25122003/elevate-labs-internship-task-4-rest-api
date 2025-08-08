import requests

url = "http://127.0.0.1:5000/users"

# POST - Add user
data = {"id": "1", "name": "Ganesh"}
response = requests.post(url, json=data)
print("POST:", response.json())

# GET - Get users
response = requests.get(url)
print("GET:", response.json())

# PUT - Update user
update_data = {"name": "Ganesh Y"}
response = requests.put(f"{url}/1", json=update_data)
print("PUT:", response.json())

# DELETE - Delete user
response = requests.delete(f"{url}/1")
print("DELETE:", response.json())

# GET again
response = requests.get(url)
print("GET after delete:", response.json())