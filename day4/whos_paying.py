import random
print("Who's gonna pay for todays bill?")
#collecting the people names
people_names=input("Please give all the names seperated by 'comma and space'.\n ")
#storing in lists as split method is returing the names seperated by ', and space"
people_lists=people_names.split(", ")
#length of people
number_of_people=len(people_lists)
#generating the random number between 0 and number of people
random_number=random.randint(0,number_of_people-1)
#fetching the people name listed in lists
person_to_pay=people_lists[random_number]
#print the final message
print(f"the person to pay the bill is {person_to_pay}")