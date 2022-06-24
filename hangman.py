import random
from hangmanart import stages
from hangmanart import logo
from hangmanwords import word_list

print (logo)
end_of_game = False
chosen_word = random.choice(word_list)
word_length  = len(chosen_word)
lives = 6
current_index = 0
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display.append("_")
display_length = len(display)
guesses = []
while not end_of_game:
    guess = input ("Guess a letter: ")
    if guess in guesses:
        print (f"Youve already guesses the letter {guess}, no lives lost.")

    for letter_index in range(0,display_length):
        if guess == chosen_word[letter_index]:
            display[letter_index] = guess
        
    print(f"{' '.join(display)}")
    if  "_" not in display:
        end_of_game = True
        print("YOU WIN! (ur still a loser tho-)")

    if guess not in chosen_word and guess not in guesses:
        print(f"You guessed the letter {guess}, its not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print ("You lose, loserrrrrrrrrrrrrrrrrrrrrrr:>")

    guesses.append(guess)

    print (stages[lives])
    








