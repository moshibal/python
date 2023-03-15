print("welcome to my pizza store")
pizza_size=input("what size pizza would you like to have? S, M, l ")
small_pizza=15
medium_pizza=20
large_pizza=25
if pizza_size=="S":
    pizza_selected="S"
    print("You have choosen small size pizza.")
    add_pepperoni=input("would you like to add pepperoni? Y or N")
    if add_pepperoni=="Y":
        small_pizza +=2
    extra_chesse=input("would you like to add extra cheese? Y or N")
    if extra_chesse=="Y":
       small_pizza+=1
       print(f"you have selected small size pizza with extra cheese. you have added extra peperoni {small_pizza-1!=small_pizza}, and the total bill is {small_pizza}")
    else:
        print(f"your bill is {small_pizza}")

elif pizza_size=="M":
    pizza_selected="M"
    print("You have choosen medium size pizza.")
    add_pepperoni=input("would you like to add pepperoni? Y or N")
    if add_pepperoni=="Y":
        medium_pizza +=3
    extra_chesse=input("would you like to add extra cheese? Y or N")
    if extra_chesse=="Y":
        medium_pizza+=1
        print(f"you have selected medium size pizza with extra cheese. you have added extra peperoni {medium_pizza-1!=medium_pizza}, and the total bill is {medium_pizza}")
    else:
        print(f"your bill is {medium_pizza}")
        
elif pizza_size=="L":
    pizza_selected="L"
    print("You have choosen large size pizza.")
    add_pepperoni=input("would you like to add pepperoni? Y or N")
    if add_pepperoni=="Y":
        large_pizza +=3
    extra_chesse=input("would you like to add extra cheese? Y or N")
    if extra_chesse=="Y":
        large_pizza+=1
        print(f"you have selected large size pizza with extra cheese. you have added extra peperoni {large_pizza-1!=large_pizza}, and the total bill is {large_pizza}")
    else:
        print(f"your bill is {large_pizza}")
else:
    print("you have provided the size we dont make it here.")
