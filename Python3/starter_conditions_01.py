hungry = False

if hungry:
    print('Go eat!')
    print('Banana?')   
else:
    print('Eat - its Dinner time : )')
    
print('Continue with your day!')


wather_temp = 22

if wather_temp <0:
    print('Freezing?')
elif wather_temp == 0:
    print('Slushy?')
elif wather_temp > 100:
    print('Boiling')
else:
    print('Liquid')


#guess a number

import random

answer = random.randint(1,10)

guess = int(input('Guess a number : '))

if guess == answer:
    print('Correct')
else:
    if guess < answer:
        print('Nope, it\'s higher!')
    else:
        print('Nope, it\'s lower!')

print('the numbner is {}'.format(answer))
