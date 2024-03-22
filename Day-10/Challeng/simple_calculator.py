f_number = int(input("Enter first number : "))
symbol = input("Type '+' or '-' or '*' of '/' : ")
s_number = int(input("Enter second number : "))

def add(f,s):
    return f+s
def sub(f,s):
    return f-s
def mul(f,s):
    return f*s
def div(f,s):
    return f/s

def result(p_symbol,first_num,second_num):
    '''
    take str(operation symbol), int ,int and do specific operation
    '''
   
        
    if p_symbol=="+":
       return add(first_num,second_num)
    elif p_symbol=="-":
       return sub(first_num,second_num)
    elif p_symbol=='*':
       return mul(first_num,second_num)
    elif p_symbol=='/':
        return div(first_num,second_num)
    else:
        return "Some inputs are missing or invalid"
    
final_result = result(p_symbol=symbol,first_num=f_number,second_num=s_number)
print(final_result)