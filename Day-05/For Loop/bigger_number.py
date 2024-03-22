numbers = input("Enter numbers :\n").split()
bigger = 0
# we can use simply max function
# print(max(numbers))

for number in numbers:
    number = int(number)
    if number>bigger:
        bigger=number
print(f"{bigger} is the bigger number.")