# weight converter
weight=float(input("enter weight"))
unit=input("enter unit in 'k' or 'l' ")

if unit=="k":
    weight=weight*2.204
    unit="kgs"
elif unit=="l":
    weight=weight/2.204
    unit="lbs"
else:
    weight="enter something"

print(f"your weight is{round(weight)}{unit}!")#ROUND USED
