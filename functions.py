def function1():
	print ("hello")

function1()

s=function1()
print (s) #prints None because the function does not return anything

#function that returns a value
def function2():
	return "I returned something"
s=function2();
print (s)