##string problems##

input = 'hello'
list1 = list(input)
print(list1)
N = len(list1)
m = N-1
reverse_list = []
for i in range(N):
    reverse_list.append(list1[m-i])
    

print(reverse_list)
reverse_string = ''.join(reverse_list)
print(reverse_string)

######

def vowel_count(word):
    vowel = 'aeiou'
    c = 0
    for i in range(5):
        if vowel[i] in word:
            c = c + 1

    print(c)



vowel_count('raunak')


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

    








