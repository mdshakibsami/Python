def add(f,s):
    return f+s
def sub(f,s):
    return f-s
def mul(f,s):
    return f*s
def div(f,s):
    return f/s

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
f_number = int(input("Enter first number : "))
for symbol in operations:
    print(symbol)
i_symbol = input("Choose any of these operation above ")
s_number = int(input("Enter second number : "))

operation = operations[i_symbol]
answer = operation(f_number,s_number)
print(f"{f_number} {i_symbol} {s_number} = {answer}")

