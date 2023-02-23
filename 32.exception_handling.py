# exception handling in python

# exception  =  an event detected during execution that interrupt the flow of a program
try:
    numerator = int(input("enter a number to divide: "))
    denominator=int (input("enter number to divide by: "))
    result=numerator/denominator
    # print(result)
except ZeroDivisionError  as e:
    print("you cant divid by zero ")
except ValueError as e:
    print("enter only numbers")
except Exception as e:
    print("somthing went wrong")
else:
    print(result)
finally:
    print("done")