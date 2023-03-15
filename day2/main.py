# number=input("please give a two digit number?\n")
# #need to change this number into the sum of two individual nums
# first_string_to_int=int(number[0])
# second_string_to_int=int(number[1])
# print(first_string_to_int+second_string_to_int)
# calculating BMI
# weight=input("please give us your weight in kilogram?\n")
# height=input("please give us your height in meter?\n")
# weight_int=int(weight)
# height_float=float(height)
# BMI=weight_int/(height_float*height_float)
# BMI_int=int(BMI)
# print(BMI_int)

# tips calculator
print("Welcome to the tip calculator.")
total_bill=int(input("What was the total bill?\n"))
tip_percent=int(input("What percentage tip would you like to give? 10, 12, 15?\n"))
total_bill_after_tips=(total_bill*tip_percent/100)+total_bill
total_people=int(input("How many people to split the bill?\n"))
bill_per_person=total_bill_after_tips/total_people
print(bill_per_person)
bill_message=f"Each person should pay: ${bill_per_person:.2f}"
print(bill_message)
