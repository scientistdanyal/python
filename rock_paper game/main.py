# add buit in module of random
import random


#options for system
options = ('rock','papar','scissor')


running = True

while running:
    player = None
    # user input space
    while player not in options:
        player = input("Enter your choice(rock, papar and scissor): ").lower()
        if player not in options:
            print("Invalid Choice")
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


    while running:    
        user_ch = ('y','n')       #choices for user
        user_in = input("Play again? (y/n) ")
    
        if user_in in user_ch:
            if user_in =='y':
                break
            else:
                running = False
        else:
            print('Invalid Choice!')    
        



print('Thanks for playing')    