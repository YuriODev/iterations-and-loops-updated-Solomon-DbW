num1 = int(input())
num2 = int(input())

def divide_without_dividing(n1, n2):
    result = 0
    remainder = 0
    while n1 >= n2:
        n1 -= n2
        result += 1
    remainder = n1
    return result, remainder

result, remainder = divide_without_dividing(num1, num2)

print(result, remainder)