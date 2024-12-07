"""
Write a function to reverse a list.
"""

def revert_list(given_list:list):
    reversed_list = []
    for element in range(len(given_list)-1, -1, -1):
        print(type(element))
        reversed_list.append(given_list[element])
    print(f"List > {given_list}\nReverse List > {reversed_list}")

random_list = ['a', 'c', 'b', 2, 3, 1]

revert_list(random_list)

"""
or
"""
random_list.reverse()
print(random_list)
