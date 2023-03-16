import requests

url = "http://140.115.197.136:8081/persons"

data = {"firstName": "VulApps", "lastName": "VulApps"}

# data = {"firstName": "Vulapps",
#         "lastName": "Vulapps",
#         "links": {
#             "seif": {
#                 "herf": "http://127.0.0.1:8080/persons/1"
#             },
#             "person": {
#                 "herf": "http://127.0.0.1:8080/person/1"
#             }
#         }
#         }

header = {"Content-Type": "application/json", "Cache-Control": "no-cache"}

r = requests.post(url=url, data=data, headers=header)

print(r.text)
print(r)
print(r.content)