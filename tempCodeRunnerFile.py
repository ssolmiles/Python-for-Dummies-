import random

guessesTaken = 0

print("What is your name?", end=" ")
myName = input()

number = random.randint(1, 20)
print("Well " + myName + ", I am thinking of a number between 1 and 20.")

for guessesTaken in range(6):
    print("Take a guess: ", end="")
    guess = input()

    if not guess.isdigit():
        print("Please enter a whole number.")
        continue

    guess = int(guess)

    if guess < number:
        print("Your guess is lower.")
    if guess > number:
        print("Your guess is higher.")
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("You guessed it right, " + myName + "! You guessed my number in " + guessesTaken + " guesses.")

if guess != number:
    number = str(number)
    print("Nope, the number I was thinking of was " + number)