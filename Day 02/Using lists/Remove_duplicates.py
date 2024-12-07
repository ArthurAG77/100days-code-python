"""
Write a function to remove duplicates from a list.
"""

def remove_duplicated(given_list):
    unique_list = []

    for i in given_list:
        if i not in unique_list:
            unique_list.append(i)

    print(unique_list)
            

remove_duplicated([2, 3, 5, 2, 1, 5])

