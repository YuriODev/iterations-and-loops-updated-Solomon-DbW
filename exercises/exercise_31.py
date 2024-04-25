num_Of_Temps = int(input())
temp1 = int(input())
min_temp = temp1
for i in range(num_Of_Temps - 1):
    temp = int(input())
    if temp < min_temp:
        min_temp = temp

below_minus_15 = 'Yes' if min_temp < -15 else 'No'

print(min_temp)
print(below_minus_15)