import random
print("enter your frineds name separated by comma :")
names = input()
name = names.split(",")
rand = random.randint(0,len(name)-1)
who_will_pay = name[rand]
print(f"{who_will_pay} will pay the bill today.")