#global
import time
import threading

def print_n():
	n=1
	while(True):
		print (n)
		time.sleep(1) #sleeping, no cpu

def print_m():
	m=2
	while(True):
		print (m)
		time.sleep(2) #sleeping, no cpu

tn=threading.Thread(target=print_n)
tn.start()
tm=threading.Thread(target=print_m)
tm.start()
print ("i got executed")