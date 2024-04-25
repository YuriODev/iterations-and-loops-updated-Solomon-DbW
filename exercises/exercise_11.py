upper_bound = int(input())
total = 0

for i in range(1, upper_bound + 1):
    total += i/(i + 1)

print(f"{total:.2f}")