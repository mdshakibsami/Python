#Problem-03

age = int(input("Enter your age: "))

if age>=60:
    print("Senior Citizen")
elif age>=20:
    print("Adult")
elif age>=13:
    print("Teenager")
else:
    print("Child")