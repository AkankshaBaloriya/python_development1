# time module methods
# .time, .ctime, .localtime, .strptime, .strftime, .asctime, .
import time
# ctime------------------------------------------------------------------
print(time.ctime(1676270097.1100001))    #this convert the seconds into time date month and all

# time-------------------------------------------------------------------
print(time.time())        #this convert proper time into seconds

# combine .time and .ctime
print(time.ctime(time.time()))

# localtime-----------------------------------------------------------------
a=time.localtime()     #this show time with full details
print(a)

# strftime--------------------------------------------------------------------
local_time=time.strftime("%B %d %Y %H :%M:%S",a)
print(local_time)               #this strftime is used to print particular tume structure choossen from localtime

# strptime-----------------------------------------------------------------
time_string="20 April 2020"
b=time.strptime(time_string,"%d %B %Y")  
print(b)              #this shows the particular time in structure form

# asctime-------------------------------------------------------------------
time_tuple=(2020,4,20,4,20,0,0,0,0)
time_string=time.asctime(time_tuple)
print(time_string)                  #this shows the time in a proper formate
