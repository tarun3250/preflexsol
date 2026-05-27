import requests

API_url="https://jsonplaceholder.typicode.com/users"

def fetch_users():
    try:
        response=requests.get(API_url,timeout=5)
        if response.status_code==200:
            return response.json()
            
        else: 
            print("failed to fetch users")
            return []

    except requests.exceptions.RequestException:
        print("api request failed")
        return []
