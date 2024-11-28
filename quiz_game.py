print("welcome to my question answer game")


question = input ("would you like to play? ")
if question.lower() != "yes":
    quit()
else:
    print("lets play")

score = 0
quize1 = input("what is the meaning of cpu? ")
if quize1.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
quize2 = input ("what is the meaning of gpu? ")
if quize2.lower() == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")
quize3 = input("define ip? ")
if quize3.lower() == "internet protocal":
    print("correct")
    score += 1
else:
    print("incorrect")
quize4 = input ("meaning of ram? ")
if quize4.lower() == "random access memory":
    print("corret")
    score += 1
else:
    print("incorrect")
print("total score"  +  str((score)/4 * 100) + "%.")
