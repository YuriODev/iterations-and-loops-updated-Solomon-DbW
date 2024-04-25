num1 = int(input())
num_Of_Prints = int(input())

for _ in range(num_Of_Prints):
    print(num1, end=" " if _ < num_Of_Prints - 1 else "")