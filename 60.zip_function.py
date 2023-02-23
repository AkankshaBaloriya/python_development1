# zip(*iterables)= aggregate elements from two or more iterables(list,tuples,sets.etc.)
                # creates a zip object with paired elements stored in tuples for each element
                
username=["dude","bro","mister"]
passwords =("a&jdd","asd23","guest")

user=list(zip(username,passwords)) #list/dict/tuple() just to typecast it tuple into list

for i in user:
    print(i)
    