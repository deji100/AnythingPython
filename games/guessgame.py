import random

secret_number = random.randint(1, 9)
num_guessed = 0
print("Let's play a game called guess.")

while True:
    name = input('Enter name: ')
    guess = int(input('Guess: '))
    if guess != secret_number:
        if num_guessed == 9:
            print('Game over.')
            break
        num_guessed += 1
    else:
        num_guessed -= 1
        if num_guessed == 1:
            print('Game over.')
            break
        # print('Wrong guess, try again.')
    # else:
    #     continue
    #     print('Congratulations! You guessed the secret number', str(secret_number))
    #     break
print('secret number:',secret_number)
