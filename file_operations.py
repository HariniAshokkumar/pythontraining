#reading a file
myfile = open("test_file.txt","r")
print (myfile.read())
myfile.close()

#writing a file
#recreates the file if it already exists (which means no error)
writeFile = open("writeFile.txt","w")
writeFile.write ("Hey there! You wrote something!\nThere's a next line too!") #\n to write multiple lines
writeFile.close()

#converting contents into a list
myfile = open("test_file.txt","r")
a=myfile.readline()
print (a.split(" "))
print (a.partition(" "))
myfile.close()

#writing a list to file
writeFileList = open("writeFileList.txt","w")
list_a=["hey","look","list"]
for x in list_a:
	writeFileList.write(x+"\n")
writeFileList.close()

#file operations without close()
with open("writeFileList2.txt","w") as file:
	list_b=["new","list","yay!"]
	for x  in list_b:
		file.write(x+"\n")