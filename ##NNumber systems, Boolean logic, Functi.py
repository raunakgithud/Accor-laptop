##NNumber systems, Boolean logic, Functions###

def binary_to_decimal(binary_str):
    decimal = 0
    length = len(binary_str)
    for i, digit in enumerate(binary_str):
        power = length - i - 1
        decimal += int(digit) * (2 ** power)
    return decimal

binary_num = "101101"
print(binary_to_decimal(binary_num))


integers = [-2, -1, 0, 1, 2]
for num in integers:
    print(num)
