import random

computer = random.randint(1,100)
while True:
    try:
        player = int(input("Guess a number between (1 to 100):"))
        if computer > player:
            print("too low")
        elif computer < player:
            print("too high")
        else:
            print("you won!") 
            break
    except ValueError:
        print("please enter a valid number:")

