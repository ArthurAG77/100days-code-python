"""
Write a function to find the intersection of two lists. 
"""

def intersection(listA, listB):
    list3 = [x for x in listA if x in listB]
    return list3

def set_intersection(listA, listB):
    return list(set(listA) & set(listB))

array = [x for x in range(0, 25) if x > 0]
array2 = [x for x in range(15, 30) if x > 15]


print(intersection(array, array2))
print()
print(set_intersection(array, array2))
