# Guessing Game: Create a program that:
# Randomly generates a number between 1 and 10 (hint: use import random and random.randint).
# Asks the user to guess the number.
# Gives feedback like "Too high" or "Too low" until the user guesses correctly.


import random 

number_to_guess= random.randint(1,10)

while True:
    user_guess=int(input("Enter the number you are guessing-  "))

    if user_guess==number_to_guess:
       print(" correct guess")

    elif user_guess!=number_to_guess:
        print ("too low try again")
    
    else:
        print ("too hight, try again")

