while True:
    calc = input("Insert your calculation here: ")
    try:
        print(f"{calc} = {eval(calc)}")
        break
    except:
        print("Bruh, how did you mess up something so simple? Just type a calculation.")