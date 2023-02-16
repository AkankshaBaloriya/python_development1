# compound interest calculator
p=0
r=0
t=0

while p<=0:
    p=float(input("enter p"))
    if p<=0:
        print("p can be this less")

while r<=0:
    r=float(input("enter r"))
    if r<=0:
        print("r can be this less")
    
while t<=0:
    t=int(input("enter t"))
    if t<=0:
        print("r can be this less")

total=p*pow(1+r/100)*t

print(p)
print(r)
print(t)
print(total)


