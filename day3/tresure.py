print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Tresure island.")
print("Your mission is to find the treasure.")
direction=input("You are in tresure island, which way would you like to go? 'left' or 'right' ").lower()
if direction=="left":
    second_direction=input("you are in the sea,would you like to swim or wait? 'swin' or 'wait' ").lower()
    if second_direction=="wait":
        print("hurry, you are in final step to reach your teasures.")
        third_direction=input("you are in the big building,there are three doors,which door would you like to choose? 'red' or 'blue' or 'green' ").lower()
        if third_direction=="red" or third_direction=="blue":
            print("Sorry, the game is over, you are in the room full of snakes.")
        else:
            print("Hurry, you have found the treasure. You are rich.🤗")

    else:
        print("Sorry, the game is over, you are eaten by the shark")  

else:
    print("Sorry, the game is over, you are eaten by the sea lion")