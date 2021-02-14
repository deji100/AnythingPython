import random

secret_number = random.randint(1, 9)  # secrte number
num_guessed = 0 # number of guesses
print("Let's play a game called guess.")

while True:
    name = input('Enter name: ') # get player name
    guess = int(input('Guess: ')) # get player guess and convert to int type
    if guess != secret_number: # if guess is not equal to secret number run the next line statement
        num_guessed += 1 # increment number of guesses if guess is not equal to secret number
        if num_guessed == 9: # if number of guesses is == 9 then
            print('Game over.') # print game over and
            break # break out of the loop
    else: # if guess is equal to secret number run the next line statement
        num_guessed -= 1 # decrease number of guesses if guess is right to accommodate more users to guess
        if num_guessed == 1: # if number of guesses is 1, then 
            print('Game over.') # print game over and
            break # break out of the loop
print('secret number:',secret_number) # print secret number
