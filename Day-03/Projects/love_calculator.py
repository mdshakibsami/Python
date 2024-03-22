your_name = input("What is your name: ")
partner_name = input("What is your partner name: ")
concate_name = your_name+partner_name
print(concate_name)
lower_concate_name = concate_name.lower()

t = lower_concate_name.count("t")
r = lower_concate_name.count("r")
u = lower_concate_name.count("u")
e = lower_concate_name.count("e")
true = t+r+u+e

l = lower_concate_name.count("l")
o = lower_concate_name.count("o")
v = lower_concate_name.count("v")
e = lower_concate_name.count("e")
love = l+o+v+e
 
love_score = int(str(true)+str(love)) #used str() for easy concating.
if love_score<10 or love_score>90:
    print(f"your score is {love_score}%, you go together like coke and mentos.")
elif love_score>=40 and love_score<=50:
    print(f"your score is {love_score}%, you are alright together.")
else:
    print(f"your score is {love_score}%")


