import random

num = random.randint(1, 10)

guess = int(input('Guess a number between 1 and 10'))
# Add while loop here
while guess != num:
# incremently assign the input to guess variable; it iterates until the "guess != num"
    guess = int(input('Guess again'))

print('You win!') 