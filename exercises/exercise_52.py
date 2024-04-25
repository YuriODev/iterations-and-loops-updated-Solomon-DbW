a = int(input())
b = int(input())

while a % 2 != 0 and b <= a:
    print(a, end=" ")
    a -= 2

a = a + 1

while b <= a:
    print(a, end=" ")
    a -= 2