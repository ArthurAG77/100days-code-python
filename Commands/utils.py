def ask_str(input_str:str, exception_message:str):
    try:
        word = str(input(f"{input_str}"))
        if word == '' or word == ' ':
            return False
        else:
            return word
    except:
        print(f"{exception_message}")

def ask_int(input_str:str, exception_message:str):
    try:
        integer = input(f"{input_str}")
        if integer == '' or integer == ' ':
            return True
        elif integer.lower() == "x":
            return False
        else:
            return int(integer)
    except:
        print(f"{exception_message}")

if __name__ == "__main__":
    ask_str('a', 'b')
