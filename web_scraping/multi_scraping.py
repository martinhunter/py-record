import threading
import time
import queue
import multiprocessing
import gevent
import requests
from gevent import monkey
monkey.patch_all()  # turn IO into async funcs

link_list=[]
link_list.append('www.baidu.com')
# append 1000 links
headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


class myThread(threading.Thread):
	'''多线程类'''
    def __init__(self,name,link_range):
        super().__init__(self)
        self.name = name
        self.link_range = link_range

    def run(self):
        print("starting")
        thread_method(self.name,self.link_range)

    @staticmethod
    def thread_method(threadName,link_range):
        for i in range(link_range[0],link_range[1]+1):
            try:
                r = requests.get(link_list[i],headers=headers)
                print(r.status_code)
            except Exception as e:
                print(threadName,'Error: ',e)

thread_list=[]
link_range_list=[(0,200),(201,400),(401,600),(601,800),(801,1000)]

for i in range(1,6):
    thread = myThread("Thread-"+str(i),link_range_list[i-1])
    # start correspond to run() in myThread class
    thread.start()
    thread_list.append(thread)

for t in thread_list:
    # thread.join() to abort till the thread ends
    t.join()

# threading.thread only -> each thread func runs 200 times and ends individually.
# thread with queue -> data is distributed to all threads,and threads end simultaneously.

class queuedThread(threading.Thread):
	'''队列类'''	
    def __init__(self,name,q):
        self.name=name
        self.q = q

    def run(self):
        while True:
            try:
                queue_method(self.name,self.q)
            except:
                break
            
    def queue_method(threadName,q):
        url = q.get(timeout=2)
        try:
            r = requests.get(url,headers=headers)
            print(r.status_code)
        except Exception as e:
                print(threadName,'Error: ',e)



workQueue = queue.Queue(1000)
thread_list2 = []

for i in range(6):
    thread= queuedThread("queue-"+str(i),workQueue)
    thread.start()
    thread_list2.append(thread)

for url in link_list:
    workQueue.put(url)

for t in thread_list2:
    t.join()



# multiprocessing
print(multiprocessing.cpu_count())

class myProcess(multiprocessing.process):
	'''多线程类'''	
    def __init__(self,q):
        self.q = q

    def run(self):
        while not self.q.empty():
            process_method(self.q)

    def process_method(q):
        url = q.get(timeout=2)
        try:
            r = requests.get(url,headers=headers)
            print(r.status_code)
        except Exception as e:
            print(url,'Error: ', e)
workQueue2 = multiprocessing.Queue(1000)

for url in link_list:
    workQueue2.put(url)
    
for i in range(0,3):
    p = myProcess(workQueue2)
    p.daemon = True
    p.start()
    p.join()

# use (multiprocessing) Pool and queue to dynamically allocate quantity of process.if Pool is not full,it will generate a new process to handle new request,else new request will have to wait.
'''线程池'''

def pool_method(q):
    while not self.q.empty():        
        url = q.get(timeout=2)
        try:
            r = requests.get(url,headers=headers)
            print(r.status_code)
        except Exception as e:
            print(url,'Error: ', e)

manager = multiprocessing.Manager()
workQueue3 = manager.Queue(1000)

pool2 = multiprocessing.Pool(processes=3)
for i in range(4):
    # use async to create unblocking process
    pool1.apply_async(pool_method,args=(workQueue3))
    # with pool1.apply(pool_method,args=(workQueue3)),process0 will run and other process will only start till process0 finishes executing.

pool2.close()
pool2.join()


# coroutine,uses gevent module
'''协程'''
def coroutine_method(index):
    coroutine_id = "Coroutine- " + str(index)
    while not self.q.empty():        
        url = q.get(timeout=2)
        try:
            r = requests.get(url,headers=headers)
            print(r.status_code)
        except Exception as e:
            print(url,'Error: ', e)

def sp():
    for url in link_list:
        workQueue4.put_nowait(url)
workQueue4 = gevent.queue.Queue(1000)
gevent.spawn(sp).join()
gevent_list = []
for i in range(10):
    gevent_list.append(gevent.spawn(coroutine_method,i))
gevent.joinall(gevent_list)
