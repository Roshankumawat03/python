import requests

# while True:
    # data = requests.get("https://www.facebook.com/")
# data = requests.get("https://dummyjson.com/users")

data = requests.get("https://www.facebook.com")

with open("fb.html", "w") as file:
    file.write(data.text)

# print(data.url)
# print(data.text)
# abc = data.json()
# print(abc)

