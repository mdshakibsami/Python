import random
from hangman_words import word_list
from hangman_art import logo
print(logo)
#chose a word
chosen_word = random.choice(word_list)
print(chosen_word)
word_len = len(chosen_word)

# blank spaces
display = []
for _ in chosen_word:
    display+='_'
# take a character input
end_of_game = True
lives = 6
while end_of_game:
    character = input("Enter a caracter: ")
    found_letter = False
    for positon in range(word_len):
        letter = chosen_word[positon]
        if letter==character:
            display[positon]=letter
            found_letter = True 
          
    print(display)
    from hangman_art import stages
    if found_letter==False:
        lives-=1
        if lives==0:
            end_of_game=False
            print("YOU LOSE")
        print(f"You guess wrong letter and you have {lives} left")
        print(stages[lives])
    else:
        print("You chose right letter")
    
    if '_' not in display:
        end_of_game=False
        print("YOU WON")



