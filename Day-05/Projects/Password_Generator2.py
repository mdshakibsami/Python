import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Make your password strong:\n")
number_of_letters = int(input("how many letters you want: "))
number_of_symbols = int(input("how many symbols you want: "))
number_of_numbers = int(input("how many numbers you want: "))

password_list =[]
for letter in range(1,number_of_letters+1):
    password_list.append(random.choice(letters))
for number in range(1,number_of_numbers+1):
    password_list.append( random.choice(numbers))
for symbol in range(1,number_of_symbols+1):
    password_list.append( random.choice(symbols))

password=""
random.shuffle(password_list)
for char in password_list:
    password += char
print(f"your password is :{password}")
