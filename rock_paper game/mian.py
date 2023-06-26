# add buit in module of random
import random


#options for system
options = ('rock','papar','scissor')

# user input space
player = input("Enter your choice(rock, papar and scissor: )").lower()


#generate random option for system
player_sys = random.choice(options)

print(f'User: {player}')
print(f'System: {player_sys}')

# statmenets
if player == player_sys:
    print('Match tie')
elif player == 'papar' and player_sys == 'rock':
    print('You won')
elif player == 'rock' and player_sys == 'scissor ':
    print('You won')
elif player == 'scissor' and player_sys == 'paper':
    print('You won') 
else:
    print('you lose')