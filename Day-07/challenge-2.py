import random
word_list = ["shakib","samiya","srabon","rock"]
chosen_word = random.choice(word_list)
print(chosen_word)
word_len = len(chosen_word)

character = input("Enter a letter: ")

display = []

for _ in chosen_word:
    display+="_"

for position in range(word_len):
    letter = chosen_word[position]
    if letter==character:
        display[position]=letter
print(display)
