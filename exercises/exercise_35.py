n = int(input())
num = 10 * (10 ** (n-1))
s = 10 ** (n-1)
for i in range(num-1,s-1, -2):
    print(i, end=" ")
print('\n')