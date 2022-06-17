#This is the Hangman Game
import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  o   |
      |
      |
      |
=========''','''

  +---+
  |   |
  o   |
  |   |
      |
      |
=========''','''

  +---+
  |   |
  0   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  o   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant baboon badger bat bear beaer camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole momkey moose mouse mule newt otter owl pamda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloath snake spider stork swan tiger toad trout turkey tuttle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    #This function return a random word from the specified list
    wordIndex = random.randint(0,len(wordList) -1)
    return wordList[wordIndex]
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #replace blanks ith correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1]
    for letter in blanks: # show secret word with blanks
        print(letter, end=' ')
    print()
def getGuess(alreadyGuessed): #returns the letter the player entered making sure he did not enter something else
    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('please enter a single letter')
        elif guess in alreadyGuessed:
            print('You hae already guessed that letter. Choose again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('please enter a LETTER')
        else:
            return guess
def playAgain(): # This function returns true if the player wants to play again
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    #let the player take a guess
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetter = False
                break
        if foundAllLetters:
            print('Yes! The secret word is " '+ secretWord + ' "! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        #check to see if the player has made too many guesses
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses! \nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break




