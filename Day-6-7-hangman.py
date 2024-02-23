import random

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(' '.join(display))

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if the user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose.. The chosen word was {chosen_word}")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if the user has got all the letters.
    if "_" not in display:
        end_of_game = True
        print("You win!!")

    # Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
