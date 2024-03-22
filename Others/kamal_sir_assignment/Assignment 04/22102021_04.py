#function with no arguments and return value:
def power():
    n=int(input("Enter a the base: "))
    a=int(input("Enter a the power "))
    power_of_base=1;
    while a>0:
        power_of_base = power_of_base*n
        a-=1
    return power_of_base
x = power()
print(x)