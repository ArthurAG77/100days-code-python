"""
Write a function to count the number of vowels in a string.
"""

import sys
sys.path.append(r'C:\Users\Mestre do Universo\Desktop\100 days code')

from Commands.utils import ask_str


def vowels_counter(word:str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    c = 0
    if word is False:
        pass
    for char in word:
        if char.lower() in vowels:
            c += 1
    return c

while True:
    print("\nPress enter to exit\n")
    word = ask_str("Insert word here: ", "Please, just words or phrases")
    if word is False:
        break
    else:
        print(f"the word {word} has {vowels_counter(word)} vowels")