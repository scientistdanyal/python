import random



options = ('rock','papar','scissor')

player = input("Enter your choice(rock, papar and scissor)").lower()

player_sys = random.choice(options)

print(f'User: {player}')
print(f'System: {player_sys}')


if player == player_sys:
    print('Match tie')
elif player == 'papar' and player_sys == 'rock':
    print('You won')
elif player == 'rock' and player_sys == 'scissor':
    print('You won')
elif player == 'scissor' and player_sys == 'paper':
    print('You won') 
else:
    print('you lose')