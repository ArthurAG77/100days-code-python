"""
Append data to an existing text file.
"""

import os 
from datetime import datetime

file_path = os.path.join(r"C:\Users\Mestre do Universo\Desktop\100 days code\Day 04\Using text file\writing-data.txt")

with open(file_path, 'a') as file:
    file.write(f"{datetime.now()}\n")
