target_term = int(input())

current_term = 0

value1 = 0
value2 = 1

while current_term < target_term:
    current_term += 1
    value1, value2 = value2, value1 + value2

print(value1, end=" ")
