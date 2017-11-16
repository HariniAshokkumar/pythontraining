import json

list_a=[]
dict_a={"name":"Ironman","power":"repulser"} #creating a dictionary
print (dict_a["name"])
dict_b={"name":"Batman","power":"no idea"}
list_a=[dict_a,dict_b] #this is a json data now
print (list_a)
####################################
#shallow copying
list_b=[]
dict_a={"name":"Ironman","power":"repulser"}
list_b.append(dict_a.copy())#shallow copying
dict_a["name"]="Batman"
list_b.append(dict_a.copy())
print (list_b)

#converts the list to json
#dumps takes an object and produces a string
data=json.dumps(list_a)
print (data)

#load would take a file-like object, read the data from that object, and use that string to create an object
data2=json.loads(data)
print (data2)