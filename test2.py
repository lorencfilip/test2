import random
print("Welcome to the Guessing Game!")
counter = 0
while True:
    counter += 1
    if counter == 4:
        break
    pole = []
    pole_nahodnych_cisel = random.randint(1, 10)
    print(pole_nahodnych_cisel)
    print()
guess = -1
while guess != pole:
        guess_str = input("Enter your guess: ")
        guess = int(guess_str)
x = pole
if x == guess:
        if guess == pole:
            print("spravne.")
        elif guess > pole:
            print("wrong.")
    