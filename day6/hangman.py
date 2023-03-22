import os
import random
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     ''')
from hangman_art import stages
from hangman_lists import word_lists

totallife=6
#picking the random word from the lists
random_word=random.choice(word_lists).lower()
word_len=len(random_word)

#generating the string with the number of space character for the length
guess_space=[]
for _ in range(0,word_len):
   guess_space.append("_")
print(f"the guess word is {random_word}")
end_of_game=False
wrong_guess=[]
while not end_of_game:
    user_guess=input("please give a letter? ").lower()
    os.system('clear')
    #important part in the whole code
    #to keep track of the user input word
   
   
    if user_guess in guess_space:
        print(f"The letter you choose is {user_guess} which you entered before, please give a new letter")
  
    for position in range(0,word_len):
            #getting the letter in the position at the time of looop.
            letter=random_word[position]
          
            #check
            if letter==user_guess:
                guess_space[position]=letter
    if user_guess not in random_word:
        if user_guess not in wrong_guess:
            wrong_guess.append(user_guess)
            totallife-=1
            print(f"The letter you choose is {user_guess}. This letter is not in the word, so your remaining life is {totallife} ")
            print(stages[totallife])     
        else:
            print(f"The letter you choose is {user_guess}. This letter has been choosen before and its wrong.")
            print(stages[totallife])

        
    if totallife==0:
        print("you lose")
        end_of_game=True
            
    if "_" not in guess_space:
        print("you won")
        end_of_game=True
    print(guess_space)
   

         
