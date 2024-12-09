while True:
    try:
        ask_division = input("Digit a division: ")
        eval(ask_division)
        break
    except  ZeroDivisionError:
        print("Can't divide by 0")
    except Exception as evalerror:
        print(f"An error has occured {evalerror}")