calc = []
operator = ['+', '-', '*', '/']

i = 1

while i < 4:
    try:
        if i % 2 == 0:
            ask_operator = input("Insert the operator: ") #check if is valid operator
            if ask_operator in operator:
                calc.append(ask_operator)
                i += 1
            else:
                i = i
        else:
            ask_num = float(input(f"Insert number: "))
            calc.append(ask_num)
            i += 1
    except Exception as e:
        print("Please, complete only with what the program is asking to you")
        i = i     

for index, op in enumerate(calc):
    if op == operator[0]:
        operation = calc[index-1] + calc[index+1]
    elif op == operator[1]:
        operation = calc[index-1] - calc[index+1]
    elif op == operator[2]:
        operation = calc[index-1] * calc[index+1]
    elif op == operator[3]:
        if calc[index+1] != 0:
            operation = calc[index-1] / calc[index+1]
        else:
            print("Division by zero - 404")

print(operation)

"""
Don't ask me why i did this, i just was bored
"""