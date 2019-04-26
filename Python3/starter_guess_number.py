#guess a number
import random

def run_game():
    answer = random.randint(1,20)
    print('Number between 1 and 20')
    
    guess = int(input('Make a guess : '))

    if guess == answer:
        print('Correct Answer!')
        return
    elif answer > guess:
        print('Guess higher!')
    else:
        print('Guess lower!')

    guess = int(input('Make a guess : '))

    if guess == answer:
        print('Correct Answer!')
        return
    elif answer > guess:
        print('Guess higher!')
    else:
        print('Guess lower!')

    guess = int(input('Make a guess : '))

    if guess == answer:
        print('Correct Answer!')
        return
    elif answer > guess:
        print('Guess higher!')
    else:
        print('Guess lower!')

    print('the numbner is {}'.format(answer))

run_game()
