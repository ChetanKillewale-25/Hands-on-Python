from threading import Thread
import os
import time

def square_number():
    for i in range(9):
        i*i
        time.sleep(0.1)

threads = []
num_threads = 10
#create process
for i in range(num_threads):
    p = Thread(target = square_number())
    threads.append(p)

#start
for p in threads:
    p.start()

#join
for p in threads:
    p.join()

print("End Main")
