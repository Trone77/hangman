import random

# Class definintion

class Hangman:
    '''
    This class is used to play the game hangman.
    
    Attributes:
        word_list : a list of words where a random word is chosen 
                    to be used to play the game.
        num_lives : number of incorrect guesses allowed in the 
                    game, set default to 5.
        word : random word chosen from word_list.
        word_guessed : the word guessed so far by the user.
        num_letters : the length of the word chosen.
        list_of_guesses : the list of all the letters guessed by the 
                          user.
        '''
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
    '''
    See help(Temperature) for accurate signature
    '''
    
    # method to check the if the guess is in the word
    def check_guess(self, guess):
        '''
        This method converts the guess to lower case and 
        checks if the guess is in the chosen word.
        It let's the user know the outcome and reduces the number
        of lives remaining if the guess is wrong.
        '''
        
        # convert the guess to lowercase
        guess = guess.lower() 
        
        # check if the guessed letter is in the word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    # method to ask the user for input
    def ask_for_input(self):
        '''
        This method asks the user for input and confirms if it is
        a valid or invalid input for the game.
        '''
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

def play_game(word_list):
    '''
    This function allows a user play the hangman game, using the Hangman
    Class.
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

word_list = ['banana', 'apple', 'strawberry', 'mango', 'guava']
play_game(word_list)
