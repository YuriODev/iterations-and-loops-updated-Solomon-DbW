upper_bound = int(input())
first_value = 0
second_value = 1
next_value = 0
while first_value < upper_bound:
    next_value = first_value + second_value
    first_value = second_value
    second_value = next_value
    print(first_value, end= " ")