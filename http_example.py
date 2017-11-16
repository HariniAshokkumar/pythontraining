import urllib.request
import json

with urllib.request.urlopen('http://ip.jsontest.com/') as response:
	html=response.read()
	data=json.loads(html)
	print (data["ip"])

with urllib.request.urlopen('http://google.co.in/') as response:
	html=response.read()
	googleFile=open("googleFile.html","w")
	googleFile.write(str(html)) #str() here converts bytes to string
	googleFile.close()
