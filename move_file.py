# move the file 
# replace
import os

source="copy_fileTXT"
destination="example_file.TXT"

try:
    if os.path.exists(destination):
        print("already a file there")
    else:
        os.replace(source,destination)
        print("source moved")
except FileNotFoundError:
    print("not found")

