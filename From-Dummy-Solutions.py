#Beginner Approach


#----------Dummy 1
def dummy_function_power(base, exponent = 2):
    return base ** exponent

print(dummy_function_power(3))  
print(dummy_function_power(3, 3))  

#Can be manually replace the exponent
#ex.
print(dummy_function_power(3, exponent=4))

# Output: 9 27 81 

#----------Dummy 2
i = 7 

if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i += 3

print(i) 
 # Output: 8


 #----------Dummy 3 

def dummy_summarize(*args, **kwargs):
    print("[args] Tuple Values:", args)
    print("[kwargs] Key value pair:", kwargs)

dummy_summarize(1, 2, 4, name="Norwegian", age=19)

 #----------Dummy 4     

def dummy_divide (a, b):
    if b==0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

print(dummy_divide(115, 2))

 #----------Dummy 5



a = {1 ,3,  4, 5, 7}
b = {0,2,4}
print(a^b)

# | intersection
# & intersection
# - difference 
# ^ symmetric difference  

 #----------Dummy 6


#guess the number game 

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


        
    
 #----------Dummy 7

import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()

#Boring game... Ill probably gonna look for some interesting games soon :p

#----------"Dummy 8 

products = {
    'cpu':[1000, 20],
    'charger':[300, 10],
    'monitor':[850, 15],
    'mouse':[500, 10]
}

#orders 
order= []
total= 0
#display


for items, info in products.items():
    print(f" {items} price: {info[0]} and stocks: {info[1]}")

while True: 
    customer = input("what is your order? type 'done' if finish ordering: ")

    if customer == 'done' or '':
        break

    if customer not in products: 
        print(f'{customer} is not in the products')
        continue

    if products[customer][1] <= 0:
        print(f"no stocks for{customer} ")
        continue

    order.append((customer, products[customer][0]))
    total += products[customer][0]
    print(f" {customer} is added to your cart price is {products[customer][0]}.")

    products[customer][1] -= 1


if total > 2000: 
    discount = 0.10*total
    total -= discount 
    print(f"disocunt is applied {discount} total: {total}")


print("final order:")
for item, price in order:
    print(f"  {item} - {price}")

print(f"final total {total}")


print(f'updated stock:')
for items, info in products.items():    
    print(f'item: {items} price: {info[0]} stocks {info[1]}')




#----------"Dummy 9 

#can't remember all the methods.. 
print([m for m in dir(set) if not m.startswith('__')])


#----------"Dummy 10 

