# read a file using python
# with open, read, closed
import os

try:
    with open("example_file.TXT") as file:
       print(file.read())
except FileNotFoundError:
    print("file not found")  #if the file will not exists this code will not through error but because of "try" function this will print(file not found instead)
# print(file.closed)