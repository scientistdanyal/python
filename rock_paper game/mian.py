import random



options = ('rock','paper','scissor')

player = input("Enter your choice(rock, paper and scissor)").lower()

player_sys = random.choice(options)


print(player_sys)