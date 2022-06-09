from math import perm
from ps3a import *
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    handin = hand
    maxword = ''
    maxscore = 0
    for i in range(0,HAND_SIZE):
        lwords = get_perms(hand,i)
        for word in lwords:
            score = get_word_score(word,HAND_SIZE)
            if (score > maxscore) and is_valid_word(word,hand,word_list):
                maxscore = score
                maxword = word
    return maxword

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    display_hand(hand)
    npoints = 0
    total = 0
    gamedone = 0
    while(True):
        print('current computer hand:')
        display_hand(hand)
        validword = False
        while not validword:
            word = comp_choose_word(hand,word_list)
            print(f'computer chooses {word}')
            validword = is_valid_word(word,hand,word_list)
            if word == '.' or word == '':
                validword = True
        if word != '.':
            npoints = get_word_score(word,HAND_SIZE)
            total += npoints
            print(f'{word} earned {npoints} points. Total: {total} points')
            hand = update_hand(hand,word)
            gamedone = 1
            for letter in hand:
                if hand[letter] > 0:
                    gamedone = 0 
        if word == '':
            gamedone = True
        if gamedone or word == '.':
            print(f'Total Score: {total} points')
            break
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    exit = False
    hand = deal_hand(HAND_SIZE)
    uorc = 'u'
    while not exit:
        while(True):
            inp = input("n,r or e: ")
            if inp == 'e':
                exit = True
                break
            inp2 = input('u or c: ')
            if inp not in ['n','r','e'] or inp2 not in ['u','c']:
                continue
            if inp == 'n':
                hand = deal_hand(HAND_SIZE)
                break
            if inp == 'r':
                break
            if inp2 == 'u':
                uorc = 'u'
            if inp2 == 'c':
                uorc = 'c'
        if (exit):
            break
        if inp2 =='u':
            play_hand(hand,word_list)
        if inp2 == 'c':
            comp_play_hand(hand,word_list)
    print('Thanks for playing')
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    #play_game(word_list)

    
