number = int(input())

sum = 0

number *= -1 if number < 0 else 1

while number > 0:
    digit = number % 10
    sum += digit
    number //= 10

print(sum)