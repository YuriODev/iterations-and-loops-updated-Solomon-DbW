n = int(input())
s = int(input())
count1 = 1
found = False
while n != 0:
    if n%10 == s:
        found = True
    n //= 10
    if found:
        continue
    count1 += 1
p = count1
print(p)