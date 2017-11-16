try:
	with open ("test.txt","r") as file:
		data=file.read()
		print (data);
except IOError:
	print ("File does not exist")
finally: #gets executed by default and always
	print ("Finally block... cleaning up operations...")