import os


try:
    file_path = os.path.join(r"C:\Users\Mestre do Universo\Desktop\100 days code\inexistent_file.txt")
    with open(file_path, 'r') as file:
        file.read()
except FileNotFoundError as e:
    print(f"An error has occured -> {e}")

    