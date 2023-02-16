# for loop

# basic syntax---------------------------------------------------------------------------------------------
for x in reversed(range(1, 11,2)):
    print(x)

print("happy new year!")

# use of continue and break------------------------------------------------------------------------------
for a in range(1, 21):
    if a==13:
        continue #13 will be skipped and rest will continue 14,15,16...
    # break       (it will break loop on 12, nothing will be printed after that)
    else:
        print(a)





