def is_palindrome(word:str):

    if word == "" or word == " ":
        pass
    else: 
        char_list = []
        for i in range(len(word), 0, -1):
            char_list.append(word[i-1])
        
        palindrome = ''.join(char for char in char_list).upper()

        if word.upper() == palindrome:
            print(f"The word: [{word}] is a palindrome, his reversed form is {palindrome.capitalize()}")
        else:
            print("The word isn't a palindrome")

while True:
    try:
        ask_word = str(input("Write a word to check if is palindrome: "))
        is_palindrome(ask_word)
    except AttributeError:
        print("Please, insert just words")

    

