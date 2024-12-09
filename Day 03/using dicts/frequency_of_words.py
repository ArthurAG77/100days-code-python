"""
Create a dictionary of words and their frequencies.
"""

def create_dict(sentence:str):
    dict = {}
    for word in sentence.split():
        if word in dict.keys():
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

dictionary = create_dict("O rato rato rato roeu roeu roeu a roupa roupa roupa do rei rei rei de roma roma roma")
for key in dictionary:
    print(f"The word {key} occured: {dictionary[key]} times")