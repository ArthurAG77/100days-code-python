"""
2. Write a program that generates random number between 2 integers
"""

import random

def ask_int(order:str):
    try:
        ask = int(input(f"Write the {order} integer for the range: "))
        if ask:
            return ask
    except:
        print("Please, insert integers")

while True:

    first_int = ask_int("First")
    second_int = ask_int("Second")

    if first_int > second_int:
        print("A range is like a sequence of numbers. For example, range(1, 6) gives you 1, 2, 3, 4, 5. The first number can't be greater than the second number in a range.")
    else:
        print(random.randint(first_int, second_int))
        break