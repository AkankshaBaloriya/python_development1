# Typecasting (implicit/explicit)

# str/int/bool/float
name="Akankhsa"
age=21
gpa=1/10
student=True

# way to get to know "datatype" of a variable
# {explicit type casting}--------------------------------------------------------------------------

print(type(name))
print(type(gpa))
print(type(student))
print(type (age))

# change datatype of a variable)
# integer  in float (vica versa)
age=(float(age))
print(type(age))
print(age)

# bool in string (vica verca)
student=str(student)
print(type(student))
print(student)

# int or float in bool (vica verca)
gpa=(bool(gpa))
print(type(gpa))
print(gpa)

# {implicit type casting}--------------------------------------------------------------------------------

# when value or variable is converted into different datatype automaticaly
x=2
y=2.0

x= x / y
print(x)




