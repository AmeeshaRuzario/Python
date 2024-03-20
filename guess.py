import random
ran = random.randint(1,10)
while True:
    guess=int(input("Enter the number to guess:"))
    if guess<ran:
        print("Guess is low")
    elif guess>ran:
        print("Guess is high")
    else:
        print("Guess is Correct Hurray!!")
        break
print("\n GAME OVER")
