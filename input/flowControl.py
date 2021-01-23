# A program that checks if it's raining or not and executes a set of instructions based on input
# answers given by the user

def rain():
    question1 = 'Is it raining? '
    answer = input(question1).capitalize()
    if answer == 'Yes':
        question2 = 'Do you have an umbrella? '
        answer = input(question2).capitalize()
        if answer == 'Yes':
            print('Alright, do have a nice day.')
        else:
            question3 = 'Would you like to lend my umbrella? '
            answer = input(question3)
            if answer in ['sure, thank you', 'yes, thank you']:
                print('You are welcome, do have a nice day.')
                print('You too.')
    else:
        print('Have a lovely day.')

rain()
    