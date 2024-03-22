print("Welcome to Python Pizza Deliveries!")
size = input("Size of your pizza? S or M or L: ")
bill = 0;
if size=="S" :
    bill +=15
elif size=="M":
    bill+= 20
elif size =="L":
    bill+=25
add_pepperoni = input("Do you want to add pepperoni? Y or N: ")
if add_pepperoni == "Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill+=1
print(f"Your bill is ${bill}")