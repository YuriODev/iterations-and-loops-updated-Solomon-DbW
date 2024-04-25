pounds = int(input())
CONV = 0.453

for i in range(1, pounds + 1):
    print(f"{i} {i*CONV:.2f}")