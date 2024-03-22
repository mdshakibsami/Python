
start = True
while start:
    method = input("write e to 'encrypt' or d to 'decrypt':")
    a = list("abcdefghijklmnopqrstuvwxyz")
    massege = input("Enter the massege: ")
    shift = int(input("Enter the shift number: "))

    def cipher(plain_text,shift_number,mode):
        code=''
        if mode=="d":
            shift_number*=-1
        for letter in plain_text:
            if letter in a:
                position = a.index(letter)
                new_position = position+shift_number
                new_position%=len(a)
                code+=a[new_position]
            else:
                code+=letter
        print(f" The final massged is: {code}")
    cipher(plain_text=massege,shift_number=shift,mode=method)
    stop =input("type yes if you want to go again, or type no:")
    if stop=="no":
        start=False
        print("Thank you,Goodbye")

