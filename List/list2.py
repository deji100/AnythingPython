import copy

spam = ['apples', 'bananas', 'tofu', 'cats'] # convert to string "apples, bananas, tofu, and cats"

def string(parameter):
    str1 = ''
    list1 = copy.copy(parameter)
    list1.remove('cats')
    cat = 'and cats'
    for i in list1:
        str1 += i + ', '
    str1 = f'"{str1}{cat}"'
    return str1

print(string(spam))
print(spam)