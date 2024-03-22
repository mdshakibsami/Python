import math
def can_needed(height,width,coverage):
    n=math.ceil((height*width)/coverage)
    # ceil convert into int type
    print(f"You need {n} cans of paint.")

h = int(input("Enter the height: "))
w = int(input("Enter the width: "))
c = int(input("Enter the coverage number: "))
can_needed(h,w,c)