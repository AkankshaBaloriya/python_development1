# nested loops (outer loops, inner loops)

# for loop in for loop (simple)-------------------------------------------------------------------------------------
for x in range(3):
    for b in range(1,11,):
        print(b, end="")
    print()

x=("ram, shayam, neha, priya, shriya")

for a in range(4):
    for b in x:
        print(b, end="")
    print()

# (complex)------------------------------------------------------------------------------------------------
row=int(input("enter row"))
column=int(input("enter column"))
symbol=input("enter symbol")

for x in range(row):
    for y in range(column):
        print(symbol, end="")
    print()