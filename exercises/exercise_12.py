factor = int(input())
total = 0

for i in range(100, 1000):
    if i % factor == 0:
        total += i

print(total)