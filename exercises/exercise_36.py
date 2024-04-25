num1 = int(input())
num2 = int(input())

def greatest_common_divisor(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

output = greatest_common_divisor(num1, num2)

print(output)