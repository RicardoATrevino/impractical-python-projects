import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    
    print('''Bagels, a deductive logic game.
            By Al Sweigart al@inventwithpython.com
            I am thinking of a {}-digit number with no repeated digits.
            Try to guess what it is. Here are some clues:
            When I say:             That means:
            
                Pico                 One digit is correct but in the wrong position.
                Fermi                One digit is correct and in the right position.
                Bagels               No digit is correct.

                For example, if the secret number was 248 and your guess was 843, the
                clues would be Fermi Pico.'''.format(NUM_DIGITS))


    

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'you got it!'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('fermi')
        elif guess[i] in secretNum:
            clues.append('pico')
    if len(clues) == 0:
        return "bagels"
    
    else:
        clues.sort()
        return ' '.join(clues)
    

if __name__ == '__main__':
    main()
    
    
    
while True:
    secretNum = getSecretNum()
    print(" You have {} attempts to guess the secret number".format(MAX_GUESSES))
    numGuesses = 1
    while numGuesses <= MAX_GUESSES:
        guess = ' '
        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            print('Guess #{}: '.format(numGuesses))
            guess = input('> ')
        
        clues = getClues(guess, secretNum)
        print(clues)
        numGuesses += 1
        if guess == secretNum:
            break
        
        if numGuesses > MAX_GUESSES:
            print('OUTTA GUESSES!!! DA NUMBA WAS {}'.format(secretNum))
            
    print("would you like to play again? (yes or no)")
    if not input ('> ').lower().startswith('y'):
        break
    
print("thanks for playing!")
    