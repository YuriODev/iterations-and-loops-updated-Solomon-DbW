rows = int(input())
columns = int(input())

for i in range(rows):
    string = str(i) + "\t"
    string = string * columns
    print(string)