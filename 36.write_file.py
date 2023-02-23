# write the file using python
# with open,(w) write, (a)append
text="hiiiiiiii what's up \n write somthing here\njoey,chandler,rose"  #if in file already somthing wiuld be written this "w" in with open will overwrite the file and "a"will append the text or file
with open("example_file.TXT" ,"a") as this:
    this.write(text)

