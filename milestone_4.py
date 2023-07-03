import random

# Class definintion

class Hangman:

    # class constructor
    def __init__(self, word_list, num_lives = 5):

        # attributes
        self.word_list =word_list
        self.num_lives = num_lives

        # other attributes
        self.word = random.choice(word_list)
        self.word_guessed = [''] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    # method to check the if the guess is in the word
    def check_guess(self, guess):
        
        # convert the guess to lowercase
        guess = guess.lower()
        
        # check if the guessed letter is in the word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    # method to ask the user for input
    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")
    
            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please, enter a single letter")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

hangman_game = Hangman(['banana', 'apple', 'strawberry', 'mango', 'guava'])
hangman_game.ask_for_input()
