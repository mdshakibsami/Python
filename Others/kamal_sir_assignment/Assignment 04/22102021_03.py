#function with argument and no return value:

def fact(n):
    mul=1
    while n>0:
        mul = mul*n
        n-=1
    print(f"Factorial of {n} is : {mul}")
n = int(input("Enter a number: "))
fact(n)