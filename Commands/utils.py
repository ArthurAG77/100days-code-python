def ask_str(input_str:str, exception:str):
    try:
        word = str(input(f"{input_str}"))
        if word == '' or word == ' ':
            return False
        else:
            return word
    except:
        print(f"{exception}")

if __name__ == "__main__":
    ask_str('a', 'b')