import sys
sys.path.append(r'C:\Users\Mestre do Universo\Desktop\100 days code')
from Commands.utils import ask_str

def reverse_sentence(sentence:str):
    normal_str = []
    for char in range(len(sentence)-1, -1, -1):
        normal_str.append(sentence[char])
    return ''.join(normal_str)



words = ask_str("Insert a sentence to be reversed: ", "Please, insert a sentence or a word")
reverse_words = reverse_sentence(words)

print(f"W: {words}\nR W: {reverse_words}")

