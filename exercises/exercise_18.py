num_of_days = int(input())
errors = 0

for i in range(num_of_days):
    num_of_errors = int(input())
    errors += num_of_errors

print(errors)