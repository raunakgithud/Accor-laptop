#Exception-handlingii


class valueerror(Exception):
    pass

try:
    x = int(input("put a number"))
    result = 100/x
    if x <= 0:
        raise ValueError("x should not be less than 0")
except ValueError as v:
    print(f'error is{v}')
else:
    print(result)


print("------------------------------------------------------")

try:
    value = input("Give a name")
except :
    print("name should be raunak")
else:
    if value == "Raunak":
        print(value)

print("---------------------------------------")

try:
    inp = int(input())
    if inp == 0:
        raise valueerror("0 not be accepted")
except valueerror as e:
    print(f"inp should not be zero{e}")
else:
    print(inp) 


try:
    ex = ValueError()
    ex.strerror = "value must be under 1 to 10"
    raise ex
except ValueError as e:
    print(ex.strerror)




