import random

while True:
    n = input("Level? ")
    if n.isalpha():
        continue
    elif int(n) <= 0:
        continue
    else:
        break
while True:
    guess = input("Guess: ")
    if guess.isalpha():
        continue
    else:
        n = int(n)
        guess = int(guess)
        random_n = random.randrange(1, n + 1)
        if guess > random_n:
            print("Too large!")
            print(random_n)
            continue
        elif guess < random_n:
            print("Too small!")
            continue
        elif guess == random_n:
            print("Just right!")
            break