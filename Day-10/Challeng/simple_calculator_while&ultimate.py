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

def calculator():
    f_number = float(input("Enter first number : "))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        i_symbol = input("Choose any of these operation above ")
        s_number = float(input("Enter next number : "))
        operation = operations[i_symbol]
        answer = operation(f_number,s_number)
        print(f"{f_number} {i_symbol} {s_number} = {answer}")

        continue_calculate = input("type 'y' to continue calculation with answe or type anything go star :")
        if continue_calculate =='y':
            f_number= answer
        else:
            should_continue = False
            calculator()
calculator()





