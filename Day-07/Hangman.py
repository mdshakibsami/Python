import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["shakib","samiya","srabon","rock"]
chosen_word = random.choice(word_list)
print(chosen_word)
word_len = len(chosen_word)

display = []
for _ in chosen_word:
    display+="_"

end_of_game = True
lives = 6
while end_of_game:
    character = input("Enter a letter: ")
    found_letter = False
    for position in range(word_len):
        letter = chosen_word[position]
        if letter==character:
            found_letter=True
            display[position]=letter
    print(display)

    if not found_letter:
        lives-=1
        print(stages[lives])
    if lives==0:
        end_of_game=False
        print("You Lose")

    if '_' not in display:
        end_of_game=False
        print("you won")
