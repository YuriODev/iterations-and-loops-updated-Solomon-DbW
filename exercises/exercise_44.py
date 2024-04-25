num = int(input())
num2 = int(input())
if num2 == 0:
    print("The sequence must contain at least two numbers.")

if num2 > num:
    max_index = 2
else:
    max_index = 1

while num != 0:
    num = int(input())
    