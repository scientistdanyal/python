from random import randint

n1 = int(input('Enter upper limit: '))
n2 = int(input('Enter lower limit: '))

number = randint(n1,n2)

chances = 0


while chances < 8:

    chances +=1 
    guess = int(input('Enter Your Guess: '))
    if number == guess:
        print("Congratulations You Won. The number was {}".format(number))
        break

    elif guess < number:
        print("you guessed a small number.")
    elif guess > number:
        print("You guessed is large number.")

    if chances == 7:
        print("You have run out of chances.\n")
        print("The number was {}\n".format(number))
        print("Better luck next time.")            
        break
    
