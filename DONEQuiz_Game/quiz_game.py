print("Welcome to the quiz!")

playing = input("Type yes to Start: ")

if playing != "yes":
    quit()

print("Awesome, let's continue")
score = 0

answer = input("When was the Delcaration of Indepencence signed? ")

if answer.lower() == "1776":
    print("That's correct!")
    score += 1
else:
    print("Wrong :(\n the answer is 1776")

answer = input("How many presidents have there been? ")

if answer.lower() == "45":
    print("That's correct!")
    score += 1
else:
    print("Wrong :(\n the answer is 45")

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("That's correct!")
    score += 1
else:
    print("Wrong :(\n the answer is central processing unit")

print(f"You got {score} questions correct out of 3")



            
