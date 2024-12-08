"""
Write a function to count the frequency of words in a sentence.
"""

def check_frequency(sentence:str):
    counter = 0
    words = sentence.split(" ")
    frequency = []
    for word in words:
        for j in words:
            if word == j:
                counter += 1
        if (word, counter) not in frequency:
            frequency.append((word, counter))
        else:
            pass

        counter = 0
    print(frequency)

check_frequency("é os guris né pai os guris mesmo")