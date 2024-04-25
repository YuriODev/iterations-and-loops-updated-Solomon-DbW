prev_num = int(input())
num = int(input())

if num == 0:
    print("The sequence must contain at least two numbers.")

sign_changes = 0
prev_sign = 1 if prev_num > 0 else -1  

while num != 0:
    current_sign = 1 if num > 0 else -1
    if current_sign != prev_sign:
        sign_changes += 1
    prev_sign = current_sign
    prev_num = num
    num = int(input())

print(sign_changes)
        