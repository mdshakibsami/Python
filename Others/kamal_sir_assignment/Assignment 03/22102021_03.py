#Problem-03

weight = float(input("Enter your weight in Kg: "))
height = float(input("Enter your height in meter: "))
bmi = weight/(height*height)
print(bmi)
if bmi>=30:
    print("Obesity.")
elif bmi>=25:
    print("Overweight.")
elif bmi>=18.5:
    print("Normal weight.")
else:
    print("Underweight.")