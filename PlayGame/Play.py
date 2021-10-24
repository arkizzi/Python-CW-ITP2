import random

#Creating Variables
name = 0
randOne = 0
randTwo = 0
ans = 0
realAns = 0
count = 1
rights = 0
wrongs = 0
final = 0
diff = 0
questions = 0
opOne = ['+', '-']
opTwo = ['+', '-', '*']
operatorOne = 0
operatorTwo = 0

#Title
print("  \n")
print("                            .·:*¨༺ CUSTOM_GAME ༻¨*:·.\n")

#Ask for name,difficulty and number of questions
name = input("Username : ")
print("  \n")
print("╔═══*.·:·.☽✧    ✦    ✧☾.·:·.*═══╗")
print("|  EASY    /      +      /  0 to 10 |")
print("|  MEDIUM  /    + & -    /  0 to 50 |")
print("|  HARD    /   +,- & *   / 0 to 100 |")
print("╚═══*.·:·.☽✧    ✦    ✧☾.·:·.*═══╝\n")
print("E - EASY     M - MEDIUM     H - HARD\n")
diff = input("State your difficulty : ")
print("  \n")
questions = int(input("Number of questions : "))

#Generating random numbers and loop 
print("                  ✧･ﾟ: *✧･ﾟ:* ✧*:GAME STARTﾟ✧ ✧･ﾟ: *✧･ﾟ:* ✧\n")
while (count <= questions):
    if (diff == "E"):
        randOne = random.randrange(0,11)
        randTwo = random.randrange(0,11)
        realAns = randOne + randTwo
        print(randOne,"+",randTwo," = ? ")
        print("  \n")
        ans = int(input("Your answer : "))
        print("  \n")
        if (ans == realAns):
            print("◉ RIGHT ◉")
            rights = rights + 1
            print("  \n")
        else:
            print("⊗ WRONG ⊗")
            print("Right answer : ",realAns)
            wrongs = wrongs + 1
            print("  \n")
    elif (diff == "M"):
        randOne = random.randrange(0,51)
        randTwo = random.randrange(0,51)
        operatorOne = random.choice(opOne)
        realAns = eval(str(randOne) + operatorOne + str(randTwo))
        print(randOne,operatorOne,randTwo," = ? ")
        print("  \n")
        ans = int(input("Your answer : "))
        print("  \n")
        if (ans == realAns):
            print("◉ RIGHT ◉")
            rights = rights + 1
            print("  \n")
        else:
            print("⊗ WRONG ⊗")
            print("Right answer : ",realAns)
            wrongs = wrongs + 1
            print("  \n")
    elif (diff == "H"):
        randOne = random.randrange(0,101)
        randTwo = random.randrange(0,101)
        operatorTwo = random.choice(opTwo)
        realAns = eval(str(randOne) + operatorTwo + str(randTwo))
        print(randOne,operatorTwo,randTwo," = ? ")
        print("  \n")
        ans = int(input("Your answer : "))
        print("  \n")
        if (ans == realAns):
            print("◉ RIGHT ◉")
            rights = rights + 1
            print("  \n")
        else:
            print("⊗ WRONG ⊗")
            print("Right answer : ",realAns)
            wrongs = wrongs + 1
            print("  \n")
    count = count + 1

#Results
print("                  ✧･ﾟ: *✧･ﾟ:* ✧*: RESULTS ﾟ✧ ✧･ﾟ: *✧･ﾟ:* ✧\n")
print("Name = ",name)
print("  \n")
print("Number of right answers : ",rights)
print("Number of wrong answers : ",wrongs)
print("  \n")
print("You've got ",rights,"out of ",questions," !")
final = int((rights / questions ) * 100)
print("                           *✧･ﾟ:* ✧*:",final,"%ﾟ✧ ✧･ﾟ: *✧･ﾟ\n")
print("RETURNING TO MENU. . .")
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import Main
