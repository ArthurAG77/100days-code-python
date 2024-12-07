import random

while True:
    random_integer = random.getrandbits(32)
    print(f"Random generated number: {random_integer}")
    restart = input("Click enter to generate again, or insert N to stop: ").upper()
    if restart == "N":
        break

