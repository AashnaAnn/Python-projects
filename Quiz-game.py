print("Welcome to my computer quiz!")

playing=input("Do you want to play? ")
score=0

if playing.lower()!="yes":
    quit()

print("Okay! Let's play...")

answer=input("What does CPU stand for? ")
if answer.lower()=="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does GPU stands for ")
if answer.lower()=="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does RAM stand for? ")
if answer.lower()=="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does PSU stand for? ")
if answer.lower()=="power supply":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does TCP stand for? ")
if answer.lower()=="transmission control protocol":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does UDP stand for? ")
if answer.lower()=="user datagram protocol":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("You got "+str(score)+" questions correct!")
print("You got "+str((score/6)*100)+"%.")

