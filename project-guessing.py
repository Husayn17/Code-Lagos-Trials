import random

def compare_number(numbers, user_guess):
    wrongright = [0,0] #wrong, then right
    for i in range(len(numbers)):
        if numbers[i] == user_guess[i]:
            wrongright[1]+=1
        else:
            wrongright[0]+=1
    return wrongright

if __name__=='__main__':
    playings = True #Play the game
    numbers = str(random.randint(0,99)) #random 2 digit number
    guesses = 0

    print('Lets play a Guessing Game!\nI will generate a number, and you would have to guess the numbers one digit at a time.\nFor every number in the wrong place, you get a wrong.\nFor every one in the right place, you get a right.\nThe game ends when you get 2 rights.\nType exit at any time to exit.') #Explanation

    while playings:
        user_guess = input('Give me your best guess!')
        if user_guess == 'exit':
            break
        wrongrightcount = compare_number(numbers, user_guess)
        guesses+=1

        print(' You have '+ str(wrongrightcount[0]) + ' wrongs, and ' + str(wrongrightcount[1]) + ' rights.')

        if wrongrightcount[1]==2:
            playings = False
            print(' You win the game after ' + str(guesses) + '! The number was '+str(numbers))
            break #redundant exit
        else:
            print('Your guess inst quite right, try again.')

    
        
