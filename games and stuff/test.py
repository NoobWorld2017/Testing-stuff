import random

def randomNumberGame(randNum1, randNum2, TryRange1, TryRange2):

    secretNumber = random.randint(randNum1, randNum2)
    print('lets play a game')
    print('guess a number from 1 to 20')

    for guesses in range(TryRange1, TryRange2):
        try:
            guess = int(input())
        except ValueError:
            print('thats not a number')
            print('Guess again this time a number')
            continue

        if secretNumber > guess:
            print('to low Guess again')
        elif secretNumber < guess:
            print('your Guess was to high Guess again')
        else:
            break

    if secretNumber == guess:
        print('congradulations you guessed the secret number it was', str(guess))
    else:
        print('Better Luck next time the secret number was', str(secretNumber))

def main():
    randomNumberGame(1, 20, 1, 7)

if __name__ == '__main__':
    main()