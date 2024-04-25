number = int(input())

even_numbers = 1 if number % 2 == 0 and number != 0 else 0

while number != 0:
    number = int(input())
    even_numbers += 1 if number % 2 == 0 else 0

print(even_numbers - 1 if even_numbers > 0 else 0)