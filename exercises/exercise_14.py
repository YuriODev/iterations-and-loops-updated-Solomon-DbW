n = int(input())
count = 0

for i in range(n):
    num = int(input())
    count += 1 if num == 0 else 0

print(count)