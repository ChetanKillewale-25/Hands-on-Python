from multiprocessing import Process
import os
import time

def square_number():
    for i in range(100):
        i*i
        time.sleep(0.1)

process = []
num_process = os.cpu_count()
#create process
for i in range(num_process):
    p = Process(target = square_number())
    process.append(p)

#start
for p in process:
    p.start()

#join
for p in process:
    p.join()

print("End Main")

