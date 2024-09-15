import requests
from config import BASE_URL

def get(endpoint):
    response = requests.get(f"{BASE_URL}{endpoint}")
    response.raise_for_status()
    return response.json()

def post(endpoint, data):
    response = requests.post(f"{BASE_URL}{endpoint}", json=data)
    response.raise_for_status()
    return response.json()

def put(endpoint, data):
    response = requests.put(f"{BASE_URL}{endpoint}", json=data)
    response.raise_for_status()
    return response.json()

def delete(endpoint):
    response = requests.delete(f"{BASE_URL}{endpoint}")
    response.raise_for_status()
    return response.json()