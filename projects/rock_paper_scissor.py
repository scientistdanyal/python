from random import choice

choices = ['Rock', 'Paper', 'Scissors']

while True:
    print('Welcome to Rock, Paper, and Scissors')
    computer_choice = choice(choices)
    try:
        player_choice = int(input('1---Rock\n2---Scissors\n3---Paper\n4---Exit\nEnter your choice: '))
    except ValueError:
        print('Please choose a valid number.')
        continue
    
    if player_choice == 1:
        select_choice = 'Rock'
    elif player_choice == 2:
        select_choice = 'Scissors'
    elif player_choice == 3:
        select_choice = 'Paper'
    elif player_choice == 4:
        break           
    else:
        print("Enter a valid number")
        continue
    
    if select_choice == computer_choice:
        print('You chose {} and opponent chose {}....Match Tie!'.format(select_choice, computer_choice))
    elif (select_choice == 'Rock' and computer_choice == 'Scissors') or \
         (select_choice == 'Scissors' and computer_choice == 'Paper') or \
         (select_choice == 'Paper' and computer_choice == 'Rock'):
        print('You chose {} and opponent chose {}....You win!'.format(select_choice, computer_choice))
    else:
        print('You lose!')
