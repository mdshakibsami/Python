print("Welcome to SPark")
height = int (input("What is your height(cm)? "))
bill =0
if height>=120:
    print("You can ride.")
    age = int(input("what is your age? "))
    if age<18:
        print("Please,give 5$.")
        bill=5
    elif age==18:
        print("You are free!")
        bill=0
    else:
        print("Please,give 10$.")
        bill=10
    want_photo = input("Do you want to take photo? Y or N: ")
    if want_photo=="Y":
        bill+=3
    print(f"Your total bill {bill}$")
else :
    print("You can't ride.")