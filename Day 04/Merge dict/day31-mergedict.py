x = {
    "Name" : "Arthur",
    "Age" : 19
}

y = {
    "Gender" : "Man",
    "Skin-color" : "White"
}

# z = x | y -> Python 3.9 ^^
# z = {**x, **y} Python 3.5 ^^^


""" 
def merge_dicts(dictA, dictB): # Python 2
    z = dictA.copy()
    z.update(dictB)
    return z
    
"""

print(merge_dicts(x, y))