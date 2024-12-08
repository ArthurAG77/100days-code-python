"""
Write a function to convert a list of words into a sentence.
"""

def list_to_sentence(list):
    sentence = ' '.join(word for word in list)
    print(sentence)
list_of_words = ["zaga", "bla", "gordo"]
