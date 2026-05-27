import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

# print(response)
data=response.json()
# print(data)
# print(type(data))
# print("the first user data is", data[0])
# print(data[0]["name"])
for user in data:
    print(user["name"])