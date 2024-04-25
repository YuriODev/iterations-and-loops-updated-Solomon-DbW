max_speed = 0
min_speed = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

num_Of_Cars = int(input())
slower_Than_30 = 0

for i in range(num_Of_Cars):
    speed = int(input())
    if speed > max_speed:
        max_speed = speed
    if speed < min_speed:
        min_speed = speed
    if speed <= 30:
        slower_Than_30 += 1

print(max_speed - min_speed)
print(slower_Than_30)