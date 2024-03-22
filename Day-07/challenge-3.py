import random
word_list = ["shakib","samiya","srabon","rock"]
chosen_word = random.choice(word_list)
print(chosen_word)
word_len = len(chosen_word)

display = []
for _ in chosen_word:
    display+="_"

end_of_game = True
while end_of_game:
    character = input("Enter a letter: ")
    for position in range(word_len):
        letter = chosen_word[position]
        if letter==character:
            display[position]=letter
    print(display)

    if '_' not in display:
        end_of_game=False
    print("you won")
