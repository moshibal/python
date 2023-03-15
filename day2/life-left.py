# creating a life remaining apps
time_to_live=80
your_age=input("Please give your age?\n")
age_int=int(your_age)
life_left_to_live_in_years=time_to_live-age_int
life_left_to_live_in_months=life_left_to_live_in_years*12
life_left_to_live_in_days=life_left_to_live_in_years*365
message=f"your life left in years is {life_left_to_live_in_years}, in months is {life_left_to_live_in_months}, and in days is {life_left_to_live_in_days}."

print(message)