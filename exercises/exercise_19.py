num = int(input())
sequence = ""

for i in range(10, 100):
    if ((i // 10) ** 2 + (i % 10) ** 2) % num == 0:
        sequence += str(i) + ", "

print(sequence)