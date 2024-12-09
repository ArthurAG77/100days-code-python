import os

file = os.path.join(r"C:\Users\Mestre do Universo\Desktop\100 days code\Day 04\Using text file\calculate avarege\nums.txt")

sum = 0
avg = 0
c = 0

with open(file, "r") as fp:
    for line in fp.readlines():
        strip_lines = line.split()
        try:
            for i in strip_lines:
                c += 1
                sum += float(i)
        except:
            pass

avg = sum/c

print(avg)