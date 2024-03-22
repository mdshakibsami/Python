def format_name(f_name,l_name):
    full_name=(f_name+' '+l_name).title()
    return f"The full name is : {full_name}"
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
formated_nam=format_name(first_name,last_name)
print(formated_nam)