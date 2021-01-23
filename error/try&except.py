def spam(divider):
    try:
        value = 10/divider
        return value
    except:
        print('division by zero error.')

print(spam(2))
print(spam(5))
print(spam(0))
print(spam(3))