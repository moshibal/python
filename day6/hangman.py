#start the game
#hold count of life
#generate the ramdom word

#check of the input is in the generated random word
 #if yes, fill the gap
 #else decrease the life
import random
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     ''')
totallife=5
word_lists=words = ['Apple', 'Angel', 'Beach', 'Brown', 'Basic', 'Bread', 'Camera', 'Circle', 'Candle', 'Cherry','Coffee', 'Dance', 'Donut', 'Dress', 'Earth', 'Email', 'Energy', 'Fruit', 'Flower', 'Forest', 'Garden', 'Guitar', 'Honey', 'Happy', 'Heart', 'Hotel', 'Island', 'Ivory', 'Jungle', 'Jacket','Laptop', 'Lemon', 'Lounge', 'Market', 'Museum', 'Nature', 'Orange', 'Office', 'Pencil', 'Piano','Purple', 'Rocket', 'School', 'Season', 'Square', 'Summer', 'Temple', 'Tomato', 'Travel', 'Winter','Absolute', 'Apartment', 'Beautiful', 'Cinnamon', 'Delicate', 'Ecosystem', 'Fascinate', 'Gorgeous', 'Happiness', 'Incredible','Jubilant', 'Knowledge', 'Lavender', 'Magnific', 'Necessary', 'Obsessed', 'Pleasant', 'Quarrelsome', 'Rational', 'Satisfaction','Terrific', 'Understand', 'Victorious', 'Wonderful', 'Xylophone', 'Yesterday', 'Zealous']

#picking the random word from the lists
random_word=random.choice(word_lists).lower()
word_len=len(random_word)

#generating the string with the number of space character for the length
guess_space=[]
for _ in range(0,word_len):
   guess_space.append("_")
print(f"the guess word is {random_word}")
end_of_game=False
while not end_of_game:
    user_guess=input("please give a letter? ").lower()
    #important part in the whole code
    for position in range(0,word_len):
        #getting the letter in the position at the time of looop.
        letter=random_word[position]
        #check
        if letter==user_guess:
            guess_space[position]=letter
    if "_" not in guess_space:
        print("you won")
        end_of_game=True

   

         
