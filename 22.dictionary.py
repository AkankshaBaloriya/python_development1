# dictionary  =  a colllection of {key:value} pairs 
                #ordered and changable. No duplicates allowed in it

capitals={"india":"delhi",
          "china":"beiking",
          "usa":"washington",}

# methods for dictionary(dir ,help, get,update,pop,popitem,clear,keys,values,items)

# dir---------------------------------------------------------------------
a=dir(capitals)
print(a)

# help---------------------------------------------------------------------
# a=help(capitals)
# print(a)

# get-----------------------------------------------------------------------
print(capitals.get("india"))

if capitals.get("india"):
    print("available")
else:
    print("not available")

# update---------------------------------------------------------------------

a=capitals.update({"japan":"berlin"})
print(capitals)

a=capitals.update({"india":"mumbai"})
print(capitals)

# pop-------------------------------------------------------------------------
(capitals.pop("india"))
print(capitals)

# popitem---------------------------------------------------------------------
# it pop the latest key vlue player
capitals.popitem()
print(capitals)

# clear-----------------------------------------------------------------------
# print(capitals.clear())
# print(capitals)

# keys------------------------------------------------------------------------
a=capitals.keys()
print(a)

for key in capitals.keys():
    print(key)
# values----------------------------------------------------------------------
a=capitals.values()
print(a)

# items(resemble a 2d lists)---------------------------------------------------
for key, value in capitals.items():
    print(f"{key} and {value}")