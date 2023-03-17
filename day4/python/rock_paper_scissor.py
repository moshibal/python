import random
# Rock
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("let's play rock paper scissors with the computer.")
#for player
player=(input("Please choose 0 for rock, 1 for papper and 2 for scissors. "))
if player=="0":
    print(f"you have choosen rock\n {rock}")
elif player=="1":
    print(f"you have choosen paper\n {paper}")
elif player=="2":
    print(f"you have choosen scissors\n {scissors}")
else:
    print("please play the game according to the rule.")


#for computer
computer= str(random.randint(0,2))
if computer=="0":
    print(f"computer have choosen rock \n {rock}")
elif computer=="1":
    print(f"computer have choosen paper \n {paper}")
elif computer=="2":
    print(f"computer have choosen scissors \n {scissors}")

#condition to decide winner
if player==computer:
    print("You both have choosen same thing, which makes it draw.")
elif player=="0" and computer=="1":
    print("Computer have won, as paper beats rock.")
elif player=="0" and computer=="2":
    print("You have won, as rock beats scissors.")
elif player=="1" and computer=="0":
    print("Computer have won, as paper beats rock.")
elif player=="2" and computer=="0":
    print("Computer have won, as rock beats scissors.")
elif player=="1" and computer=="2":
    print("Computer have won, as scissors beats papper.")
elif player=="2" and computer=="1":
    print("You have won, as scissors beats papper.")