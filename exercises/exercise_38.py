n = int(input())

min = n % 10
max = n % 10
while n > 0:
    digit = n % 10
    if digit < min:
        min = digit
    elif digit > max:
        max = digit
    n //= 10
range = max - min
if range % 2 == 0 and range != 0:
    print("True")
else:
    print("False")
