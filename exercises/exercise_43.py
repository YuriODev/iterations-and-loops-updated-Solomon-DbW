num = int(input())

biggest, second_biggest = num, 0

while num != 0:
    num = int(input())

    if num > biggest:
        second_biggest = biggest
        biggest = num

    elif num > second_biggest:
        second_biggest = num

print(second_biggest)