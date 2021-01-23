value = 0
user = int(input('Enter number: '))

while value != 1:
    def collatz(number):
        if number % 2 == 0:
            return number // 2
        elif number % 2 == 1:
            return 3 * number + 1
        # value += number

    collatz(user)