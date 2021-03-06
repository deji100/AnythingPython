import random, string


def password(length, num=False, strength='weak'):
    """Length of password, num if you want a number and 
    strength(weak, strong, very strong)
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letter = lower + upper
    dig = string.digits  
    punct = string.punctuation
    pwd = ''
    length -= 2
    if strength == 'weak':
        print('Weak Password.')
        if num:
            for i in range(2):
                 pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(lower)
    elif strength == 'strong':
        print('Strong Password.')
        if num:
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(letter)
    elif strength == 'very':
        print('Very Strong Password.')
        ran = random.randint(2, 4)
        length -= ran
        if num:
             for i in range(ran):
                 pwd += random.choice(dig)
        for i in range(ran):
            pwd += random.choice(punct)
        for i in range(length):
            pwd += random.choice(letter)
    pwd = list(pwd)
    random.shuffle(pwd)
    return ''.join(pwd)


print(password(5, num=True))
print(password(10, num=True, strength='strong'))
print(password(20, num=True, strength='very'))
