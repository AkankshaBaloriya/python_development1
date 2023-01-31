# rock papaer scissor game  with computer
import random
# --------------------------------------------------------------------------------------------

# options=("rock","paper","scissor")
# # you=None
# comp=random.choice(options)

# # while you not in options: (mine one)
# while True:
#     you=input("enter here")
#     if you==comp:
#         print("its a tie")
#         print(comp)
#     elif you=="rock" and comp=="paper":
#         print("you loose")
#         print(comp)
#     elif you=="paper" and comp=="rock":
#         print("you win")
#         print(comp)
#     elif you=="scissor" and comp=="paper":
#         print("you win")
#         print(comp)
#     elif you=="paper" and comp=="scissor":
#         print("you loose")
#     elif you=="rock" and comp=="scissor":
#         print("you win")
#         print(comp)
#     elif you=="scissor" and comp=="rock":
#         print("you loose")
#         print(comp)
#     else:
#         break

# by bro code

options=("rock","paper","scissor")


running=True

while running:
    you=None
    comp=random.choice(options)

    while you not in options:
            you=input("enter here")

    print(you)
    print(comp)

    if you==comp:
        print("its a tie")
    elif you=="rock" and comp=="scissor":
        print("you win")
    elif you=="paper" and comp=="rock":
        print("you win")
    elif you=="scissor" and comp=="paper":
        print("you win")
    else:
        print("you loose")