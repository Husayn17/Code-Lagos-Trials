names = input('Enter the name of 2 people:')
score = 0
for character in names:
    if character in 'aeiou':
        score += 5
    if character in 'friend':
        score += 8
    if score > 100:
        print('Best of Friends')
print ('Your Friendship is worth:',score)
