"""
DAEMON THREAD : dies when the main thread dies, after exiting the main thread all the thread dies so the
worker method & while Ture Loop no longer gets invoked.
"""


from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(q,lock):
    while True:
        value = q.get()
        #processsing
        with lock:
            print(f"in {current_thread().name} get {value}")
        q.taskdone()

if __name__ == "__main__":

    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target = worker, args=(q, lock))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()
    print("End Main")


