print("Welcome to my Acronym Quiz")

playing = input("Do you want to play?")


if playing.lower() != "yes":
    quit() #the program will quit if they type anything other than yes

print("Okay! Let's play😄")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!✅")
    score += 2 #increment score if answer is correct
else:
    print("Incorrect❌")

answer = input("What does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    print("Correct!✅")
    score += 2
else:
    print("Incorrect❌")

answer = input("What does RAM stand for ")
if answer.lower() == "random access memory":
    print("Correct!✅")
    score += 2
else:
    print("Incorrect❌")

answer = input("What does URL stand for? ")
if answer.lower() == "uniform resource locator":
    print("Correct!✅")
    score += 2
else:
    print("Incorrect❌")

answer = input("What does SQL stand for? ")
if answer.lower() == "structured query language":
    print("Correct!✅")
    score += 2
else:
    print("Incorrect❌")


print("You got " + str(score) + " questions correct!") #covert score to string
print("You got " + str((score/5) * 100) + "%.")
