"""
https://www.100daysofcode.io/learn/python/day-26

calcular anagrama

formula: n!/Fi! 
n -> Total de letras
Fi -> quantas vezes cada letra aparece

devo fazer
fatorial do len da palavra

contar quantas vezes uma letra se repete e fazer o fatorial
calcular o fatorial
armazenar

multiplicar oque está armazenado

então 
realizar n!/Fi! 
retornar resultado
"""

def factorial(num):
    calc = []
    fact = 1

    for i in range(num, 0, -1):
        calc.append(i)

    for i in calc:
        fact *= i
    
    return fact

def frequency_letters(sentence:str):
    counter = 0
    frequency = []
    for word in sentence:
        for j in sentence:
            if word == j:
                counter += 1
        if (word, counter) not in frequency:
            frequency.append((word, counter))
        else:
            pass
        counter = 0
    
    return frequency

def anagram(word:str):
    try:
        n = factorial(len(word))
        fn = 1
        for tuple in frequency_letters(word):
            fi = factorial(tuple[1])
            fn *= fi
        anagram = n/fn
        return f"The anagram of: {word} is {anagram}" 
    except Exception as e:
        print(f"Something doesn't occured as planned {e}")
    

print(anagram("banana"))