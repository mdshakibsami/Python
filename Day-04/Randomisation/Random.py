# for using random(),we have to import random file
import random
# let's generate a randome number between 1 to 100 including both
rand_int = random.randint(1,100)
print(rand_int)
# let's use random function by defualt
#this only generate floating point value between 0 and 1
rand= random.random()
print(rand)
# if we want between 0 to x=5, [0,5)
randR = random.random()*5
print(round(randR))