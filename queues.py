#queues and pipes should be used for interprocess communication
from multiprocessing import Queue
import time
import threading

myq=Queue()
myq.put("hi")
print (myq.get(timeout=2)) #timeout=True (also non-blocking) will also work; or else the get statement keeps waiting until there's content in the queue

q2=Queue()

def data_gen():
	while (True):
		data="Data created"
		q2.put(data)
		time.sleep(2)

def data_accept(threadname):
	while(True):
		print (q2.get(True)+threadname)

tg=threading.Thread(target=data_gen)
tg.start()
#note the additional comma in the argument list. it is extremely important
ta1=threading.Thread(target=data_accept,args=("thread 1",)) 
ta1.start()
ta2=threading.Thread(target=data_accept,args=("thread 2",))
ta2.start()
ta3=threading.Thread(target=data_accept,args=("thread 3",))
ta3.start()