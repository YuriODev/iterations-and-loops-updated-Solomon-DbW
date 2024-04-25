n = int(input())
count = 0

for i in range(1, n+1):
    j = i
    

    if j % 10 == 0:
        count += 1

    elif j < 10:
        count += 1

    elif j < 100 and j % 10 == j // 10:
            count += 1

    elif j < 1000 and  j % 10 == j // 100:
            count += 1

    elif j < 10000 and j % 10 == j // 1000 and j // 10 % 10 == j // 100 % 10 and j // 100 % 10 == j // 1000:
            count += 1

    elif j < 100000 and j % 10 == j // 10000 and j // 10 % 10 == j // 100 % 10 and j // 100 % 10 == j // 1000 % 10 and j // 1000 % 10 == j // 10000:
            count += 1

print(count)