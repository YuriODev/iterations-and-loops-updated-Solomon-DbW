hours = int(input())
cells = 1

while hours > 2:
    cells *= 2
    hours -= 3
print(cells)