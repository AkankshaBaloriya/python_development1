# email slicer
email=input("enter the full name")

index=email.index("@")#(index before @ is a built in method)

username=email[:index]
domain=email[index:]

print(f"your username is {username} and domain is {domain} .")
