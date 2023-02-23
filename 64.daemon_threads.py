# deamon threads =a thread that runs in the background, not important for program to run your program will not wait for deamon threads to complete before exiting non-demon threads cannot normally be killed,stay alive task is complete

# ex.background tasks, garbage collection, waiting for input, long running process

import threading
import time

def timer():
    print()
    print()
    count=0
    while True:
        time.sleep(1)
        count+=1
        print("logged in for:", count)
        
b=threading.Thread(target=timer,daemon=True)
b.start()

b=input("enter a number here")
print(b)