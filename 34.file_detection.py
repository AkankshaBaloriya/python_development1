# file detection
# exists, isfile, isdir
import os

path ="example_file.TXT"        #enter path here

if os.path.exists(path):            #"exists" used to check weather file exists or not
    print("exist")
    if os.path.isfile(path):    #"isfile" used to check weather it is a file 
        print("yes this is a file")    
    elif os.path.isdir(path):           #"isdir" used to check weather it is a directory
        print("it is a directory")
else:
    print("dosent exists")