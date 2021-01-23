filename = open('password.txt')
readfile = filename.read()
print('Enter your password.')
password = input('Password: ')
if password == readfile:
    print('Access granted')
else:
    print('Access Denied.')