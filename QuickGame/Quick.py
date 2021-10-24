import random
import pickle

#Creating Variables
name = 0
rights = 0
wrongs = 0
final = 0
yn = 0
fo = 0

#Creating functions
def qandAs():
    randOne = 0
    randTwo = 0
    ans = 0
    realAns = 0
    count = 1
    global rights
    global wrongs
    global name
    global final
    global results
    print("                  ✧･ﾟ: *✧･ﾟ:* ✧*:GAME STARTﾟ✧ ✧･ﾟ: *✧･ﾟ:* ✧\n")
    while (count <= 5):
        randOne=random.randrange(0,11)
        randTwo=random.randrange(0,11)
        realAns = randOne + randTwo
        print(randOne," + ",randTwo," = ? ")
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
    print("                  ✧･ﾟ: *✧･ﾟ:* ✧*: RESULTS ﾟ✧ ✧･ﾟ: *✧･ﾟ:* ✧\n")
    print("Name = ",name)
    fo = open("quicklist.txt","w")
    fo.write(name)
    fo.close
    print("  \n")
    print("Number of right answers : ",rights)
    print("Number of wrong answers : ",wrongs)
    print("  \n")
    print("You've got ",rights,"out of 5 !")
    final = int((rights / 5) * 100)
    print("                           *✧･ﾟ:* ✧*:",str(final),"%ﾟ✧ ✧･ﾟ: *✧･ﾟ\n")
    fo = open("quicklist.txt","w")
    fo.write(str(final))
    fo.close

#Title
print("  \n")
print("                            .·:*¨༺ QUICK_GAME ༻¨*:·.\n")

#Ask for name
name = input("Name : ")
print("  \n")                          

#Generating random numbers and loop
qandAs()

#Replay
print("Play again? Y / N")
yn = input("  ")
print("  \n")
if (yn=="N"):
    import os,sys,inspect
    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir) 
    import Main
elif (yn=="Y"):
    qandAs()
    import os,sys,inspect
    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir) 
    import Main
