"""
Write a program to find the largest of three numbers.
bruh
"""

numbers = []
temp = 0

for i in range(0, 3):
    try:
        ask_int = int(input("Digit a number: "))
        numbers.append(ask_int)
    except:
        print("Just integers numbers pls")

for i in numbers:
    if temp < i:
        temp = i

if numbers.count(temp) == len(numbers):
    print(f"{numbers} are all the same numbers")
else:
    print(f"The largest number in {numbers} are {temp}")