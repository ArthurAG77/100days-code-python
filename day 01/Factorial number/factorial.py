"""Write a function to calculate the factorial of a number."""
from time import sleep

def factorial(num):
    calc = []
    fact = 1

    for i in range(num, 0, -1):
        calc.append(i)

    for i in calc:
        fact *= i
        print(f"{i} x ", end="", flush=True)
        sleep(.2)
    print(f" = {fact}", flush=True)

if __name__ == "__main__":
    factorial(11)


"""
https://www.100daysofcode.io/learn/python/day-15
"""