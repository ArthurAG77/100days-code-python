from time import sleep

while True:
    try:
        print("\nTo leave, press enter")
        ask_num = input("Digit a integer to check if is even or odd: ")
        if ask_num == "":
            bye = "leaving..."
            for _ in bye:
                print(f"{_}", end="", flush=True)
                sleep(.2)
            break
        else:
            num = int(ask_num)
    except:
        print("Just integers friend, try again")

    
    if num % 2 == 0:
        print(f"{num} is even")
        sleep(.2)
    else:
        print(f"{num} is odd")
        sleep(.2)
