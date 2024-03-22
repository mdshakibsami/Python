print("Welcome to SPark")
height = int (input("What is your height(cm)? "))
if height>=120:
    print("You can ride.")
    age = int(input("what is your age? "))
    if age<18:
        print("Please,give 5$.")
    elif age==18:
        print("You are free!")
    else:
        print("Please,give 10$.")

else :
    print("You can't ride.")