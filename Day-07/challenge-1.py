import random
word_list = ["shakib","samiya","srabon","rock"]
chosen_word = random.choice(word_list)
print(chosen_word)
character = input("Enter a letter: ")
for letter in chosen_word:
    if letter == character:
        print("Matched")
    else:
        print("Not Matched")