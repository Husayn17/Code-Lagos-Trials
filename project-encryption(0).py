alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 5
new_message = ''

message = input('Please enter a message: ')

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position+key)%26
        new_character = alphabet[new_position]
        new_message += new_character
    else:
        new_message += character
    
print ('Your new message is',new_message)
