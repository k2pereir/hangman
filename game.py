import random 
import nltk
#nltk.download('words')
from nltk.corpus import words
import time

#guess sequence 
def guess_sequence(): 
    guess = input(("Guess a letter: "))
    while len(guess) != 1:
        guess = input(("Please enter a single letter: "))
    return guess

#guessing correctly sequence
def right_letter_sequence(guess, word, current):
    temp = current.split()
    for i in range(len(word)):
        if word[i] == guess:
            temp[i] = guess
    temp = " ".join(temp) 
    return temp

def main(): 
    #get a random word
    list_of_words = words.words()
    word = random.choice(list_of_words)

    #im a cheater
    print(word)

    #rules 
    input("Press enter to flip through the rules")
    print("Hey! Welcome to Hangman!", end='')
    input()
    print("A random word has been chosen for you to guess", end='')
    input()
    print("You get 6 mistakes before the man is, well, fully drawn", end='')
    input()
    print("Anyways good luck", end='')
    input()

        #stage iterations 
    man = ['''
    *---*
    |   |
        |
        |
        |
        |
    =========''','''
    *---*
    |   |
    O   |
        |
        |
        |
    =========''', '''
    *---*
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    *---*
    |   |
    O   |
   /|   |
        |
        |
    =========''','''
    *---*
    |   |
    O   |
   /|\  |
        |
        |
    =========''','''
    *---*
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''','''
    *---*
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

    correct_messages = ["Ate.", "It's illegal to be this good at something", "Go crazy", "Ok genius", "You're doing great", "Live, laugh, love words", "Michelin star chef", "Worrrddddssss", "Words of encouragement", "You're a natural"]
    incorrect_messages = ["Ohhh that's not right", "Unfortunate", "Poor guy", "You're doing kind of badly", "Ok get better", "Watch out", "Yikes", "You're not doing great", "Getting charred", "You're not a natural", "Words of discouragement"]

    #initializing game
    current = ""
    for i in range(len(word)):
        current = current + "_"
        current = current + " "
    incorrect = 0
    myguess = ""

    #game loop
    while incorrect <= 6:
        print(man[incorrect])
        print(current)
        guess = guess_sequence()
        if guess in word: 
            print(random.choice(correct_messages))
            time.sleep(1)
            current = right_letter_sequence(guess, word, current)
            myguess = myguess + guess
        else: 
            print(random.choice(incorrect_messages))
            time.sleep(1)
            incorrect = incorrect + 1
        if myguess == word: 
            print("Yippee! You win! You're right, the word was " + word)
            break 
        if incorrect == 6:
            print("I'm so sorry for your loss, better luck next time")
            print("The word was " + word)

if __name__ == "__main__": 
    main()