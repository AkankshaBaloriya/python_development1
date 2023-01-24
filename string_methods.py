# string methods
# len/insert/append/add/remove/pop/replace/find/rfind//capitalize/upper/lower/isdigit/isalpha/count/

# len method(len method indicate"lenght of variable)--------------------------------------------------------

a=input("enter yout name")
b=len(a)   #(this could be printed this way as well)
print(b)
print(len(a))

# find method (find the keyword's index (it find first occurance))----------------------------------------------------------------------

a=input("enter statment")

b=a.find("akki")
print(b)

# rfind method (this find keyword's last occurance)---------------------------------------------------------

a=input("enter statement")
b=a.rfind("akki")
print(b)

# capitalize(it capitalice the variable value's first word)--------------------------------------------------

a=input("enter words")#gor printing another variable can be created same as given in "len"
print(a.capitalize())

# upper(it capitalizr allthe words of variable value)---------------------------------------------------------

a=input("enter name")
b=a.upper()
print(b)

# lower(lower allthe character of variable)------------------------------------------------------------------

a=input("enter here")
print(a.lower())

# isdigit (print boolean "true" if characters of variable are digits)--------------------------------------

a=input("enter number")
b=a.isdigit()
print(b)

# isalpha (print boolean "true" if characters of variable are alphabet)-------------------------------------

a=input("enter alphabet")
print(a.isalpha())

#count(this cout the  number  humber how many times the word or character ---------------------------
# is present in thevalue of varianle)------------------------------------------------------

a=input("enter the stuff")
print(a.count("akki"))

#replace(this repalce the  value or character from another)--------------------------------------------------

a=input("enter statment here")  
print(a.replace("akki","akanksha"))



