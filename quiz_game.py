# quiz game

q=("what is your name",
   "where do you live",
   "what do you do",
   "your faviourite color")

o= (("a. akki","b. tanu","c. aash","none"),
    ("a. sanwer","b. indore","c. delhi","none"),
    ("a. er.","b. singer","c. both","none"),
    ("a. red","b. purple","c. blue","none"))

a=("a","b","c","b")

guesss=[]
score=0
qun=0

for  qu in q:
    print("--------------------")
    print(qu)
    for op in o[qun]:
        print(op)
    
    guess=input("enter (a,b,c):").lower()
    guesss.append(guess)
    if guess == a[qun]:
        score+=1
        print("correct")
    else:
        print("wrong")
        print(f"{a[qun]} is correct answer")
    qun+=1

print("-------------------")
print("answer",end=" ")
for an in a:
    print(an , end=" ")
print()

print("guess",end=" ")
for guess in guesss:
    print(guess , end=" ")
print()

score=int(score/len(q)*100)
print(f"{score}%")


