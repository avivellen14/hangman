HANGMAN_ASCII_ART = """ 
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
"""
MAX_TRIES = 6
print ("Welcome to the game Hangman" , HANGMAN_ASCII_ART , "\n" , MAX_TRIES)

guessed_letter = str(input ("Guess a letter: "))
if guessed_letter.isalpha() and len(guessed_letter) >1:
    print ("E1")
elif not guessed_letter.isalpha() and len(guessed_letter) == 1:
    print ("E2")
elif not guessed_letter.isalpha() and len(guessed_letter) > 1:
    print ("E3")
elif guessed_letter.isalpha() and len(guessed_letter) == 1:
    print (guessed_letter.lower())
else:
    print ("oops ")


guessed_word = input("Please enter a string: ")
guessed_word_length = len (guessed_word) 
first_part_word = guessed_word[:guessed_word_length//2].lower()
second_part_word = guessed_word[guessed_word_length//2 : ].upper()
new_word =  first_part_word + second_part_word
print (new_word)

guessing = input("Please enter a word: ")
guessing_length = len(guessing)
print ("_ " * guessing_length)
