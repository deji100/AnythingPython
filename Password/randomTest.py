import random, string

pwd = ""
for i in range(8):
    digits = list(string.digits)
    choice = random.choice(digits)
    pwd += choice
print(pwd)