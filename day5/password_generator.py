#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#random letters from the lists and storing in lists
list_of_letters=[]
for sym in range(0,nr_letters):
    list_of_letters.append(random.choice(letters))

#random number formm number lists and storing in lists
list_of_number=[]
for num in range(0,nr_numbers):
    list_of_number.append(random.choice(numbers))
#random symbol from the lists and storing in list
list_of_symbol=[]
for sym in range(0,nr_symbols):
    list_of_symbol.append(random.choice(symbols))
#merging all the lists together
merge_all=list_of_letters+list_of_number+list_of_symbol
#shuffling the lists
random.shuffle(merge_all)
#joining all the items in the lists
password="".join(merge_all)
print(f"the temporary password generated is {password}")