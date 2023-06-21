import random

# Creating a list of five fruits
word_list = ['banana', 'apple', 'strawberry', 'mango', 'guava']

# printing out the list
print(word_list)

# choosing a random word from the list

word = random.choice(word_list)

print(word)

# taking a single alphabet input from user

guess = input('Enter a letter: ')

# checking if user input is valid

if len(guess) == 1 and guess.isalpha() == True:
    print('Good Guess!')
else:
    print('Oops! That is not a valid input.')