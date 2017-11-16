list_a=["hi","hello",True,0,1.1]
print (list_a)
print (list_a[2])
list_b=["nothing",list_a] #multidimensional array
print (list_b)
list_a.append("new") #appending new items
print (list_a)

Garage = "Ferrari", "Honda", "Porsche", "Toyota" 
print (Garage) 
for each_car in Garage:
	print(each_car)

#checking if an element is present in a list can be done in an if statement
if ("Honda" in Garage):
	print ("Honda exists!")