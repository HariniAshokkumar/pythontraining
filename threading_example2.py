#global
import time
import threading
#passing arguments
def print_n(duration,message):
	while(True):
		print (message)
		time.sleep(duration) #sleeping, no cpu

tn=threading.Thread(target=print_n,args=(2,"hi",))#passing a tuple of arguments
tn.start()
print ("i got executed after 2 secs")