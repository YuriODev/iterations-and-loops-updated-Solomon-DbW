number = int(input())
for i in range(number):
    for j in range(number):
        if i == j:
            print(0, end="\t")
        elif i < j:
            print(1, end="\t")
        else:
            print(-1, end="\t")

    print('')