import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    
    s = ''
    for letter in secret_word:
        if letter in letters_guessed:
            s += letter
        else:
            s += '*'
    return s


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    
    s = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            s += letter
    return s


def print_starting_message(secret_word):
    print('Welcome to Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')


def print_guess_message(guesses_left, letters_guessed):
    print('--------------')
    print('You have', guesses_left, 'guesses left.')
    print('Available letters:', get_available_letters(letters_guessed))
    

def input_with_check(with_help):
    inp = input('Please guess a letter: ')
    if len(inp) == 1 and (inp.isalpha() or with_help and inp == '!'):
        return True, inp.lower()
    return False, inp


def choose_a_letter_to_reveal(secret_word, available_letters):
    choose_from = ''
    for letter in secret_word:
        if letter in available_letters and letter not in choose_from:
            choose_from += letter
    new = random.randint(0, len(choose_from) - 1)
    revealed_letter = choose_from[new]
    return revealed_letter


def unique_letters(secret_words):
    unique = []
    for letter in secret_words:
        if letter not in unique:
            unique.append(letter)
    return unique


def score(guesses_left, secret_word):
    return guesses_left + 4 * len(unique_letters(secret_word)) + 3 * len(secret_word)


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    
    print_starting_message(secret_word)
    
    guesses_left = 10
    letters_guessed = []
    
    while guesses_left > 0 and not has_player_won(secret_word, letters_guessed):
        print_guess_message(guesses_left, letters_guessed)
        
        inp_correct, inp = input_with_check(with_help)
        if not inp_correct:
            print('Oops! That is not a valid letter. Please input a letter from the alphabet:', get_word_progress(secret_word, letters_guessed))
            continue
        
        if inp == '!':
            revealed_letter = choose_a_letter_to_reveal(secret_word, get_available_letters(letters_guessed))
            print('Letter revealed:', revealed_letter)
            letters_guessed.append(revealed_letter)
            print(get_word_progress(secret_word, letters_guessed))
            guesses_left -= 3
            continue
        
        if inp in letters_guessed:
            print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))
            continue
        
        letters_guessed.append(inp)
        
        if inp in secret_word:
            print('Good guess:', get_word_progress(secret_word, letters_guessed))
        else:
            print('Oops! That letter is not in my word:', get_word_progress(secret_word, letters_guessed))
            if inp in 'aeiou':
                guesses_left -= 2
            else:
                guesses_left -= 1
    
    print('--------------')
    if guesses_left <= 0:
        print('Sorry, you run out of guesses. The word was', secret_word)
    else:
        print('Congratulations, you won!')
        print('Your total score for this game is:', score(guesses_left, secret_word))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!
