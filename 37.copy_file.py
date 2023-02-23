# copy the file in python

# copyfile()  =  copies contents of a file
#  copy() = copyfile + permission mode + destination can be a directory
#  copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile("example_file.TXT","copy.TXT") #COPIED IN copy.TXT