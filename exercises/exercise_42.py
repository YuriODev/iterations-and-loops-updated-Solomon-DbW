num = int(input())

count = 0

previous_num = num

while num != 0:
    num = int(input())

    if num < previous_num:
        count += 1

    previous_num = num

print(count)