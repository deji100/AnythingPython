
def collatz(number):
        if number % 2 == 0:
            return number // 2
        elif number % 2 == 1:
            return 3 * number + 1

user = int(input('Enter number: '))

while True:
    print(collatz(user))