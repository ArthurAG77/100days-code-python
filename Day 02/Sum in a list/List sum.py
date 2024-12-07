import sys
from time import sleep
sys.path.append(r'C:\Users\Mestre do Universo\Desktop\100 days code')
from Commands.utils import ask_int

calc = []

def sum_list(list_of_ints:list):
    operation = 0
    for int in list_of_ints:
        operation += int
    print(f"\nThe sum of the list {list_of_ints} is:")
    for index,num in enumerate(list_of_ints):
        if index > 0:
            print(f"+ {num} ", end="", flush=True)
            sleep(.4)
        else:
            print(f"{num} ", end="", flush=True)
            sleep(.4)
    print(f"= {operation}")


while True:
    print("Press x to exit")
    number = ask_int("Insert a natural number to add to the list: ", "Please just numbers here")
    if type(number) == int:
        calc.append(number)
    elif number is True:
        sum_list(calc)
        break
    elif number is False:
        break
