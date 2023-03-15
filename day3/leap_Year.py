year=int(input("please type the year to see if the given year is leap year or not?\n"))
if year % 4==0:
    print("the given year is cleanly divisible by 4, let divide by 100 again to make sure its a leap year")
    if year % 100 !=0:
         print("the given year is not cleanly divisible by 100, so its a leap year.")
    else:
         print("the given year is also cleanly divisible by 100, so its not a leap year yet.")
         if year % 400 == 0:
              print("the given year is also cleanly divisible by 400, so its a leap year.")
         else:
              print("the given year is not cleanly divisible by 400, so its not a leap year.")
else:
    print("the given year is not cleanly divisible by 4, so its not a leap year.")