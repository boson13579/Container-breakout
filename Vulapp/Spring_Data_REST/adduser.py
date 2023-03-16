import requests

url = "http://140.115.197.136:8081/persons"

data =  {"firstName": "VulApps", "lastName": "VulApps"}

header = {"Content-Type": "application/json", "Cache-Control": "no-cache"}

r = requests.post(url=url, data=data, headers=header)

print(r.text)
print(r)
print(r.content)