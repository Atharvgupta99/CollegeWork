import random
a = random.randint(1, 100)
b = 0
print("Guess a number between 1 and 100:")
while b != a:
    b = int(input("Enter your guess: "))    
    if b < a:
        print("Too low! Try again.")
    elif b > a:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it correctly.")
