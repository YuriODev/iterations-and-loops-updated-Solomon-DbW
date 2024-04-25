number = int(input())
total = number
terms = 1

while number != 0:
    number = int(input())
    total += number
    terms += 1

average = total / (terms-1) if terms > 1 else total / terms

print(average)