height =float(input("Enter your height in meter: "))
weight = int(input("Enter your weight in kg: "))
BMI =round(weight/height**2)
if BMI<=18.5:
    print(f"your BMI is {BMI} ,you are underweight.")
elif  BMI<=25:
    print(f"your BMI is {BMI} ,you are normal weight.")
elif BMI<=30:
    print(f"your BMI is {BMI} ,you are overweight.")
elif BMI<=35:
    print(f"your BMI is {BMI} ,you are obese.")
else:
    print(f"your BMI is {BMI} ,you are clinically obese.")