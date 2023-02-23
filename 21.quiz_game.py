# # quiz game

# q=("what is your name",
#    "where do you live",
#    "what do you do",
#    "your faviourite color")

# o= (("a. akki","b. tanu","c. aash","none"),
#     ("a. sanwer","b. indore","c. delhi","none"),
#     ("a. er.","b. singer","c. both","none"),
#     ("a. red","b. purple","c. blue","none"))

# a=("a","b","c","b")

# guesss=[]
# score=0
# qun=0

# for  qu in q:
#     print("--------------------")
#     print(qu)
#     for op in o[qun]:
#         print(op)
    
#     guess=input("enter (a,b,c):").lower()
#     guesss.append(guess)
#     if guess == a[qun]:
#         score+=1
#         print("correct")
#     else:
#         print("wrong")
#         print(f"{a[qun]} is correct answer")
#     qun+=1

# print("-------------------")
# print("answer",end=" ")
# for an in a:
#     print(an , end=" ")
# print()

# print("guess",end=" ")
# for guess in guesss:
#     print(guess , end=" ")
# print()

# score=int(score/len(q)*100)
# print(f"{score}%")


# another quiz------------------------------------------------------------------------------------------

q=("what is capital of india",
   "what is national  bird of india",
   "what is cleanest city of india",
   "what language does india speak")

o=(("a. delhi","b. mumbai","c. indore"),
("a. peacock","b. sparrow","c. other"),
("a. udaipur","b. delhi","c. indore"),
("a. urdu","b. english","c. hindi"))

a=["a","a","c","c"]
scor=0
g=[]
marks=0

for x in q:
    print("-------------------------------")
    print(x)
    for op in o[scor]:
        print(op)

    

    guess=input("enter answer (a) (b) (c)").lower()
    g.append(guess)
    if guess==a[scor]:
        print("correct")
        marks+=1
    else:
        print("incorrect")
        print(f"correct answer is {a[scor]}")

    scor+=1

print(f"total mark is {marks} out of 4")