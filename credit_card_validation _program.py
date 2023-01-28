# credit card validator program (incomplete)
sum1=0
sum2=0

num=(input("enter the card number"))
num=(num.replace("-",""))
num=(num.replace(" ",""))
num=num[::-1]
# print(num)

# step-2

for x in num[::2]:
    sum1+= int(x)

# step-2

for x in num[1::2]:
    x=int(x)*2
    if x>=10:
        sum1+=(1+(x%10))


