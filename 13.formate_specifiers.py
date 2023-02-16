# formate specifiers(.2f , 10 ,>10, <10, ^10 ,+, -)

num1=3.245678
num2=5.677
num3=8.888

print(f"num 1 is {num1:.3f}")#shows number upto 3  desimal
print(f"num2 is{num2:10}")#print value in space of 10 "run code count indexes"
print(f"num3 is {num3:>10}")#print value in space more than  10 "run code count indexes"
print(f"num3 is {num3:<3}")#print value in space of less than 3 "run code count indexes"
print(f"num1 is {num1:^3}")
print(f"num3 is {num3:+3}")#make +/- sign to value {positive/negative}"