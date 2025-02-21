import requests
import json

# URL of the Flask application
url = "http://127.0.0.1:5000/bfhl"

# Data to be sent in the POST request
data = {
    "data": ["A", "b", "1", "2", "C", "d"]
}

# Making a POST request
response = requests.post(url, json=data)

# Printing the response
print("POST Response:")
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# Making a GET request
response = requests.get(url)

# Printing the response
print("\nGET Response:")
print("Status Code:", response.status_code)
print("Response JSON:", response.json())