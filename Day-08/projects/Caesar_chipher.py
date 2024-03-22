
method = input("write e to 'encrypt' or d to 'decrypt':")
a = list("abcdefghijklmnopqrstuvwxyz")
massege = input("Enter the massege: ")
shift = int(input("Enter the shift number: "))

def encrypt(plain_text,shift_number):
    encrypt_massege=''
    for letter in plain_text:
        if letter in a:
            position = a.index(letter)
            new_position =position+shift_number
            new_position%=len(a)
            encrypt_massege+=a[new_position]
        else:
            encrypt_massege+=letter
    print(f" The encypt massged is: {encrypt_massege}")


def decrypt(cipher_text,shift_number):
    decrypt_massege=''
    print(shift_number)
    for letter in cipher_text:
        if letter in a:
            position = a.index(letter)
            new_position=position-shift_number
            new_position%=len(a)
            decrypt_massege+=a[new_position]
        else:
            decrypt_massege+=letter      
    print(f"The decrypt massege is: {decrypt_massege}")

if method == 'e':
    encrypt(plain_text=massege,shift_number=shift)
elif method == 'd':
    decrypt(cipher_text=massege,shift_number=shift)
