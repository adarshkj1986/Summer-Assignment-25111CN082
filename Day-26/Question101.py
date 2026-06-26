import random
target=random.randint(1,100)
print("I have picked a number between 1 to 100")
while True:
    guess=int(input("enter the number:"))
    if guess<target:
        print("try again")
    elif guess>target:
        print("try again")
    else:
        print("you win")
        break