
"""
day 03 was a Sunday, so i studied just a little bit

Day 30 - Sort a list
Sort a list of numbers in ascending order.

"""

def bubble_sort(given_list:list):
    sorted_list = []
    for i in range(len(given_list)-1):
        for j in range(len(given_list)-1):
            if given_list[j] > given_list[j+1]:
                temp = given_list[j]
                given_list[j] = given_list[j+1]
                given_list[j+1] = temp
    print(given_list)


bubble_sort([50, 40, 30, 20, 10, 5])

# output 1 5 10 20 25 43 53