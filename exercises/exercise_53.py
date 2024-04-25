a = int(input())
b = int(input())

while a % 2 == 0 and a <= b:
    print(a, end=" ")
    a += 2
    
a = a + 1

while a <= b:
    print(a, end=" ")
    a += 2