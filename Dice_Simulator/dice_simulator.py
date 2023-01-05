import random

def roll():
    randomNumber = random.randint(1,6)
    with open("D:\Projects\Dice_Simulator\dicerolls.txt", "r") as dicePrintRepresentations:
        i = 0
        for line in dicePrintRepresentations.readlines():
            i += 1
            desiredDiceRoll = line.strip()
            if randomNumber == i:
                print(desiredDiceRoll.replace("\\n", "\n"))
            

# driver Code
def main():
    roll()
    userInput = input("This is a dice simulator, type y to roll, press any other key to quit: ")
    while userInput == "y":
            roll()
            userInput = input("type y to roll again, type any other key to quit: ")

main()
