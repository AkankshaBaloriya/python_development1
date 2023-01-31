# # random number generator
import random  #random module

# print(help(random))    #get helphow to use random module

number=random.randint(1,6)  #to print random number in that range 1 to 6
print(number)

# we can also do this insted
low =1
high=10

no=random.randint(low,high)
print(no)

#  for printing random floating point number
no=random.random()
print(no)

# print random choice from collections
options=("rock","paper","scessior")
a=random.choice(options)
print(a)

# shuffle the collections
cards=["2","4","6","8","10"]
random.shuffle(cards)
print(cards)

# numbesr gussing game---------------------------------------------------------------------------------

low=1
high=6
guess=0
number=random.randint(low,high)

while True:
    guesses=int(input(f"enter the number between{low} to {high}:"))
    guess+=1

    if guesses<number:
        print(f"{guesses} is too low")
    elif guesses>number:
        print(f"{guesses} is too high")
    else:
        print(f"{guesses} is correct")
        break

print(f"this round took you {guess} guesses ")

# one more-------------------------------------------------------------------------------------------------

# low=1
# high=6
b=random.randint(1,6)
while True:
    a=int(input("enter number"))

    if a==b:
        print(f"{a} is correct")
        break
    else:
        print(f"{a}is incurrect")



