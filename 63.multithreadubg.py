# multithreading = a flow of execution like a separate order of instructions.
# however each thread takes a turn running to achieve concurrecy
# GIL =(global interpreter lock),
# allows only on thread to hold the control of the python interpreter

# cpu bound = program/task spends most of it's time waiting for internal events
#  use multiprocessing

# io bound =progrma/task spends most of it's time waiting gor external events (user input)
# use multithreading

import threading
import time

def eat():
    time.sleep(2)
    print("we are eating here")     #if there woild be only one thread than all function will work sequence wise
    
def drink():
    time.sleep(4)
    print("we are drinking")
    
def play():
    time.sleep(6)
    print("we are playing")

x=threading.Thread(target=eat, args=())    
x.start()

y=threading.Thread(target=drink,args=())          #multi threading will make all functions work simontaniously
y.start()

z=threading.Thread(target=play,args=())
z.start()

x.join()
y.join()            #join all threads in one despite they works simontanilusly
z.join()
# eat()
# drink()
# play()

print(threading.active_count())
print(threading.enumerate())