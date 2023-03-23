from art import logo
import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
def caesar(text,number,direction):
   
    changed_text=""
    if direction=="decode":
       number*=-1
    for char in text:
        if char not in alphabet:
            changed_text+=char
        else:
            index=alphabet.index(char)
            shifted_position=index+number
            changed_text+=alphabet[shifted_position]
    print(f"the {direction}d text is {changed_text} .")
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    caesar(text,shift,direction)
    restart=input("Type 'yes' to continue.Otherwise, 'no'\n")
    if(restart=="no"):
        should_continue=False
        print("good bye.")

  