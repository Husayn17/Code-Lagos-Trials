import random

characters = 'abcdefghijklmnopqrstuvvwxyzABCDEFGHIIJKLMNOPQRSTUVWXYZ1234567890!"£$%^&*()_+-=:?><~##;'

length = input('password length?')
length = int(length)

numbers = input('number of passwords?')
numbers = int(numbers)

for p in range(numbers):
    password = ''
    for c in range(length):
        password += random.choice(characters)
    print (password)
