import random

guessesTaken = 0
print('Hello! What is your name?')
myName = input()
print('well, ' + myName + ' I am thinking of a number between 1 and 20')
number = random.randint(1,20)
while guessesTaken<6:
    print('Take a guess')
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == guessesTaken:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good! You have guessed my number in ' + guessesTaken + ' guesses')
if guess != number:
    number = str(number)
    print('Nop! the number I as thinking of is ' + number)

