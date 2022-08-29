import random
n =random.randint(1,10)
guess = int(input("Enter a number from  1-10 "))
while n!= "guess":
    if guess < n:
        print('Guess is lower')
        guess= int(input("Enter a number from  1-10 "))
    elif guess>n:
        print('Guess is higher')
        guess= int(input("Enter a number from  1-10 "))
    else:
        print("You guessed it right")
        break
