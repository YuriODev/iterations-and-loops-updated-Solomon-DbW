a = int(input())
b = int(input())

for i in range(a, b + 1):
    i_units = i % 10
    i_tens = i // 10 % 10
    i_hundreds = i // 100 % 10
    i_thousands = i // 1000

    if i_units == i_tens == i_hundreds or i_units == i_tens == i_thousands or i_units == i_hundreds == i_thousands or i_tens == i_hundreds == i_thousands:
        print(i, end=" ")


# b_units = b % 10
# b_tens = b // 10 % 10
# b_hundreds = b // 100 % 10
# b_thousinds = b // 1000