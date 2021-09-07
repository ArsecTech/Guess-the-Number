import random

cups = int(input('How many cups? '))
chances = int(input('How many chances? '))

ai_goal = random.randint(1,cups )
Line_Lenght = 15

print('-'*10)
word = 's'

for i in range(chances):
    if chances - i == 1:
        word = ''
    print(f'{chances - i} chance{word} left.')
    user_guess = int(input(f'Guess [1-{cups}]: '))

    if  user_guess == ai_goal:
        print('You gussed right.')
        break
    else:
        print('Wrong guess.')

    print('-'*Line_Lenght)

if user_guess == ai_goal:
    print('-'*Line_Lenght)
    print('You won!') 
else:
    print(f'The right answer is {ai_goal}')
    print('You lost. Sorry!')
