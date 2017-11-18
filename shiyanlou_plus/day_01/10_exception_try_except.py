filename = input("Enter file path:")

try:
    f = open(filename)
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File not found")
