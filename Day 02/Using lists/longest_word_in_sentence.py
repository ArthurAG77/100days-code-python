def find_longest_word(sentence:str):
    words_list = sentence.split()
    longest_word = ''
    for word in words_list:
        if len(longest_word) < len(word):
            longest_word = word
    print(longest_word) 

find_longest_word("O rato roeu a roupa do rei de roma")