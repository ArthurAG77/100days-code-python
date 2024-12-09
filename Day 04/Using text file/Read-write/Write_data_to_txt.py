from datetime import datetime
import os

file_path = r"C:\Users\Mestre do Universo\Desktop\100 days code\Day 04\Using text file\Read-write"
file_name = "writing-data.txt"

with open(os.path.join(file_path, file_name), 'w') as fp:
    fp.write(f"{datetime.now()}")

