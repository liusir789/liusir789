"""CSC108H1: Fall 2025 -- Assignment 1: Mystery Message Functions

Instructions (READ THIS FIRST!)
===============================

Make sure that the files a1_checker.py, a1_pyta.json, checker_generic.py
and mystery_message_game.py are in the same folder as this file
(mm_functions.py).

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students 
taking the CSC108H1 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2025 CSC108H1 Teaching Team
"""

# points earned on each occurrence of a correctly guessed consonant
CONSONANT_POINTS = 1

# cost of buying a vowel, does not depend on the number of occurrences
VOWEL_COST = 1

# points earned on each occurrence of hidden consonants at the time of
# solving the puzzle
CONSONANT_BONUS = 2

# players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# menu options
CONSONANT = 'C'  # guess a consonant
VOWEL = 'V'      # buy a vowel
SOLVE = 'S'      # try to solve the puzzle
QUIT = 'Q'       # quit the game

# symbol used for hidden characters
HIDDEN = '^'

# Game types
HUMAN = 'P1'             # one player, human
HUMAN_HUMAN = 'PVP'      # two players, human+human (player vs player)
HUMAN_COMPUTER = 'PVE'   # two players, human+computer (player vs environment)

# computer difficulty levels
EASY = 'E'  # computer plays the "easy" strategy
HARD = 'H'  # computer plays the "hard" strategy

# all consonants and all vowels
ALL_CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
ALL_VOWELS = 'aeiou'

# the order in which a computer player, hard difficulty level, will
# guess consonants
PRIORITY_CONSONANTS = 'tnrslhdcmpfygbwvkqxjz'


# We provide this function as an example.
# This function is already complete. You must not modify it.
def is_win(view: str, message: str) -> bool:
    """Return True if and only if message and view are a winning
    combination. That is, if and only if message and view are the same.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('a^^le', 'apple')
    False
    >>> is_win('app', 'apple')
    False
    """

    return message == view


# We provide this function as an example of using a function as a helper.
# This function is already complete. You must not modify it.
def is_game_over(view: str, message: str, move: str) -> bool:
    """Return True if and only if message and view are a winning
    combination or move is QUIT.

    >>> is_game_over('a^^le', 'apple', VOWEL)
    False
    >>> is_game_over('a^^le', 'apple', 'Q')
    True
    >>> is_game_over('apple', 'apple', 'S')
    True
    """

    return move == QUIT or is_win(view, message)


# Helper function for computer_chooses_solve
# This function is already complete. You must not modify it.
def half_revealed(view: str) -> bool:
    """Return True if and only if at least half of the alphabetic
    characters in view are revealed.

    >>> half_revealed('')
    True
    >>> half_revealed('x')
    True
    >>> half_revealed('^')
    False
    >>> half_revealed('a^,^c!')
    True
    >>> half_revealed('a^b^^e ^c^d^^d')
    False
    """
    num_hidden = view.count(HIDDEN)
    num_alphabetic = 0
    for char in view:
        if char.isalpha():
            num_alphabetic = num_alphabetic + 1
    return num_alphabetic >= num_hidden


# Implement the required functions below.
#
# We have provided the complete docstring (but not the body!) for the first
# function you are to write.  Write a function body for the function
# is_human.
#
# The header and docstring of is_human is an example of where and how to use
# constants in the docstring. We use the default values of constants in
# the docstring examples, but must use the constants in the function body.

def is_human(current_player: str, game_type: str) -> bool:
    """Return True if and only if current_player represents a human in a
    game of type game_type.

    current_player is PLAYER_ONE or PLAYER_TWO.
    game_type is HUMAN, HUMAN_HUMAN, or HUMAN_COMPUTER.

    In a HUMAN game or a HUMAN_HUMAN game, a player is always
    human. In a HUMAN_COMPUTER game, PLAYER_ONE is human and
    PLAYER_TWO is computer.

    >>> is_human('Player One', 'P1')
    True
    >>> is_human('Player One', 'PVP')
    True
    >>> is_human('Player Two', 'PVP')
    True
    >>> is_human('Player One', 'PVE')
    True
    >>> is_human('Player Two', 'PVE')
    False
    """
    if current_player == PLAYER_ONE and game_type == HUMAN_COMPUTER:
        return True
    
    elif game_type == HUMAN or game_type == HUMAN_HUMAN:
        return True
    
    else:
        return False

    # Complete the body of this function.

# Now define the other functions described in the handout.
# Follow the Function Design Recipe to produce complete functions for
# is_one_player_game, current_player_score, is_bonus_letter, 
# get_updated_char_view, calculate_score, next_player, is_fully_hidden,
# computer_chooses_solve, and remove_at_index.

def is_one_player_game(game_type: str ) -> bool:
    """Return True if and only if the selcted game type is one player game
    game_type is HUMAN, HUMAN_HUMAN, or HUMAN_COMPUTER.
    
    In one player game, only HUMAN is the correct one. HUMAN_HUMAN and 
    HUMAN_COMPUTER both have two players
    
    >>> is_one_player_game('P1') 
    True 
    >>> is_one_player_game('PVP') 
    False 
    >>> is_one_player_game('PVE') 
    False
    """
    return game_type == HUMAN
    
def current_player_score(player_one_score: int,
                         player_two_score: int,
                         current_player: str) -> int:
    """Return the score of the current player.
    
    the current player will be PLAYER_ONE or PLAYER_TWO
    
    current_player == PLAYER_TWO return player_one_score
    current_player == PLAYER_TWO return player_two_score
    
    >>> current_player_score(1,2,'Player One') 
    1 
    >>> current_player_score(3,4,'Player Two') 
    4
    """
    if current_player == PLAYER_ONE:
        return player_one_score
    else:
        return player_two_score

def is_bonus_letter(view: str, letter: str, message: str) -> bool:
    """Return if and only the sencond argument is a bonus letter
    bonus letters are consonants that are currently hidden
    
    bonus letter:
    1. in the message
    2. in ALL_CONSONANTS
    3. is the hidden letter(can't find it)
    
    >>> is_bonus_letter('bitter','b','bitter') 
    False
    >>> is_bonus_letter('^itter','b','bitter') 
    True 
    >>> is_bonus_letter('b^tter','i','bitter') 
    False 
    >>> is_bonus_letter('bi^ter','t','bitter') 
    False
    """
    return letter in message and letter not in view and letter in ALL_CONSONANTS

def get_updated_char_view(view: str,
                          message: str,
                          index_of_char: int,
                          guess_char:str) -> str:
    """Return the updated view string if the guess is correct,
    the updated view should be the revealed character;
    otherwise it should be the unchanged character
    from the view before the function was called.
    
    precondition:
    0 <= index <= len(message)
    
    1.the guess char not in view
    2.the guess char in message
    3.index_of_char == HIDDEN
    
    >>> get_updated_char_view('b^tter', 'bitter', 1, 'i')
    'i'
    >>> get_updated_char_view('b^tter', 'bitter', 1, 'e')
    '^'
    >>> get_updated_char_view('app^e', 'apple', 2, 'a')
    'p'
    >>>
    """
    if message[index_of_char] == guess_char:
        return guess_char
    else:
        return view[index_of_char]
    
def calculate_score(current_score: int,
                    num_of_occurrences: int,
                    move: str) -> int:
    """Return the new updated score 
    
    precondition:
    
    The move:
    guess a consonat('C'):
    buy a vowel('V'):
    
    >>> calculate_score(20,3,'V')
    19
    >>> calculate_score(5,1,'C')
    6
    >> calculate_score(6,3,'C')
    9
    """
    if move == CONSONANT:
        return current_score + (CONSONANT_POINTS * num_of_occurrences)
    elif move == VOWEL:
        return current_score - VOWEL_COST
    else:
        return current_score

def next_player(current_player: str,
                num_of_occurrneces: int,
                game_type: str) -> str:
    """Return the player to play in the next turn - player one or player two.
    
    >>> next_player('Player One', 2, 'P1')
    'Player One'
    >>> next_player('Player One', 0, 'P1')
    'Player One'
    >>> next_player('Player Two', 1, 'PVP')
    'Player Two'
    >>> next_player('Player One', 0, 'PVP')
    'Player One'
    >>> next_player('Player One', 1, 'PVE')
    'Player One'
    >>> next_player('Player One', 0, 'PVE')
    'Player Two'
    """
    if game_type == HUMAN or num_of_occurrneces >0:
        return current_player
    
    elif current_player == PLAYER_ONE:
        return PLAYER_TWO
    
    else:
        return PLAYER_ONE
        
        
def is_fully_hidden(view: str, index: int, message: str) -> bool:
    """Return true if and only if the char at the given index of the message
    isn't revealed anywhere in the view
    
    preconditon:
    0 <= index < len(message)
    >>> is_fully_hidden('^ana^a', 4, 'banana')
    False
    >>> is_fully_hidden('^pple', 0, 'apple')
    True
    >>> is_fully_hidden('^anana', 0, 'banana')
    True
    >>> is_fully_hidden('b^nana', 1, 'banana')
    False
    """
    return message[index] not in view
    
def computer_chooses_solve(view: str,
                           difficulty: str,
                           unused_consonats: str) -> bool:
    """Return true if and only if the computer follow the strategy.
    
    HARD: chooses to solve when at least half of the letters have been revealed
    or no more consonants to guess
    
    EASY: chooses to solve if there are no more consonants to guess
    
    OTHER: no solving
    >>> computer_chooses_solve('app^e', 'E', 'l')
    False
    >>> computer_chooses_solve('appl^', 'E', '')
    True
    >>> computer_chooses_solve('appl^', 'H', '')
    True
    """
    if difficulty == 'H':
        return half_revealed(view) or (unused_consonats == '')
    else:
        return unused_consonats == ''

def remove_at_index(string: str, index: int) -> str:
    """Return letters with characters at index removed.
    
    >>> remove_at_index('appl^',4)
    'appl'
    >>> remove_at_index('^itter',0)
    'itter'
    >>> remove_at_index('bitt^r',4)
    'bittr'
    >>> remove_at_index('bitt^r',4)
    
    """
    if 0 <= index < len(string):
        return string [:index] + string[index + 1:]
    return string