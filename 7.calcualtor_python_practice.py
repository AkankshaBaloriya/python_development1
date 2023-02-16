num1=int(input("enter the number 1"))
num2=int(input("enter the number 2"))
operator=input("ente the operator")
 
if  operator=="+":
    result=(f"add is{num1+num2}")
elif operator=="-":
    result=(f"minus is {num1-num2}")
elif operator=="*":
    result=(f"muntiply is {num1*num2}")
elif operator=="/":
    result=(f"divid is{num1/num2}")
else :
    result="choose right operatresul"
print(result)