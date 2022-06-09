# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
def main():
    wordlist = load_words()
    word = choose_word(wordlist)
    wordlen = len(word)
    print(f"Welcome to the game, Hangman!\nI am thinking of a word that is {wordlen} letters long.")
    print('----------')
    nguess = 8
    letters = 'abcdefghijklmnopqrstuvwxyz'
    hidden_word = ''
    for i in range(len(word)):
        hidden_word += '_'
    while(nguess > 0):
        print(f'You have {nguess} guesses left')
        print(f'Available letters {letters}')
        guess = input("Please guess a letter: ")
        if guess in word:
            for ind,let in enumerate(word):
                if guess == word[ind]:
                    hidden_word = hidden_word[:ind] + guess + hidden_word[ind+1:]
            letters.replace(guess,'')
            print(f'Good guess: {hidden_word}')
        else:
            nguess -= 1
            print(f'Oops! That letter is not in my word: {hidden_word}')
    if '_' in hidden_word:
        print('You Lose')
        print(word)
    else: 
        print('Congratulations, you win')



if __name__ == '__main__':
    main()
