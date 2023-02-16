# if/elif/else

age=int(input("enter your age"))

if age>=18:
    print("you are now signed up")
elif age<=0:
    print("get born first")
else :
    print("grow up first")

a=input("would you like something (y/n")

if a=="y":
    print("have some")
elif a =="n":
    print("please take something")
elif a=="":
    print("say something")#empty
else:
    print("okay fine")