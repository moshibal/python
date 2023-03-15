weight=int(input("please type your weight in kilogram?\n"))
height=float(input("please type your height in meter?\n"))
bmi= round(weight / height ** 2,2)

if bmi<18.5:
    print(f"your bmi is {bmi}, you are slightly underweight")
elif bmi<25:
     print(f"your bmi is {bmi}, you are normal weight")
elif bmi<30:
     print(f"your bmi is {bmi},you are over weight")
elif bmi<35:
     print(f"your bmi is {bmi},you are obese")
elif bmi>35:
     print(f"your bmi is {bmi},you are clinical obese")