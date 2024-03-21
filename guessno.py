import random
ran = random.randint(1, 10)
while True:
    guessno = int(input("Enter the guess number: "))
    if guessno > ran:
        print("Guess is high")
    elif guessno < ran:
        print("Guess is low")
    else:
        print("Guess is correct! Hurray!")
        break
print("\nGame over")



