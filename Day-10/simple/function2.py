#multiple return statements
def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "Please enter your first or last name"
    full_name=(f_name+' '+l_name).title()
    return f"The full name is : {full_name}"
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
formated_nam=format_name(first_name,last_name)
print(formated_nam)