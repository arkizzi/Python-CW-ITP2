import sys

#Creating Variables
userOpt = 0

#Title
print("                         ·:*¨༺ WELCOME TO MATH GAME ༻¨*:·.\n", sys.argv[0])
print("┊         ┊       ┊   ┊    ┊        ┊")
print("┊         ┊       ┊   ┊   ˚♡ ⋆｡˚ ❀")
print("┊         ┊       ┊   ✫")
print("┊         ┊       ♫ °")
print("┊         ⊹")
print("✽ ⋆      ┊ . ˚.")
print("❆")

#Mode selection
print("  \n")
print("╔═══*.·:·.☽✧    ✦    ✧☾.·:·.*═══╗")
print("|           QUICK GAME - Q          |")
print("|          CUSTOM GAME - C          |")
print("|        PAST GAMEPLAYS - P         |")
print("|             EXIT - E              |")
print("╚═══*.·:·.☽✧    ✦    ✧☾.·:·.*═══╝\n")
userOpt=input("What would you like to do? : ")
if (userOpt == "Q"):
    from QuickGame import Quick
elif (userOpt == "C"):
    from PlayGame import Play
elif (userOpt == "P"):
    print("test")
elif (userOpt == "E"):
    exit()
else :
    print("   \n")
    print("°•°•°•°•°•°•°•°•INVALID_INPUT!!•°•°•°•°•°•°•°•°•°•°•")
