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

data=json.dumps(list_a)
print (data)

data2=json.loads(data)
print (data2)