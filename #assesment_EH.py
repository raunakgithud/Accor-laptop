#Assesment
print("-----------------------------------")

#a = int(input("provide an integer"))
#b = int(input("give an integer"))
#result = a/b
#try:
#    a = int(input("provide an integer"))
#    b = int(input("give an integer"))
#    result = a/b
#    if b == 0:
#        raise ZeroDivisionError("Division by zero is not allowed")
#except ZeroDivisionError as z:
#    print(z)
#else:
#    print(result)

#try:
#    user_list = [1,2,3,4,5]
#    user_inp = int(input("provide an index between 0 to 4"))
#    if user_inp >= 5:
#        raise ValueError("Index out of range")
#except ValueError as v:
#    print(v)
#else:
#    print(user_list[user_inp])

#try:
#    inp = input("Provide an integer")
#    if inp is not int:
#        raise TypeError("Invalid input!Please enter an integer")
#except TypeError as t:
#    print(t)
#else:
#    print(inp)
#
#    
#

#try:
#    a = int(input("Assume a number"))
#    b = int(input("Assume the 2nd number"))
#    result = a/b
#    if a is not int or b is not int:
#        raise ValueError("incorrect format")
#    if b == 0:
#        raise ZeroDivisionError("b should not be zero")
#except ValueError as v:
#    print(v)
#except ZeroDivisionError as z:
#    print(z)
#else:
#    print(result)

#def negetivenumbererror(a):
#    try:
#        if a < 0:
#            raise negetivenumbererror("given number is negetive")
#    except negetivenumbererror as nve:
#        print(nve)
#    else:
#        print(a)
#
# 
[x for x in range(6)]

for i in range(7):
    if i%2 == 0:
        print(i,end="")


s = 'raunak'
print(s[::])  
print(s[::-2]) 

#u = "a_b_c".split("_".split)

print([[0]*3]*2)


try:
    d = int(input("provide an intiger"))
    if d < 0 and d > 10:
        raise ValueError("invalid input")
except ValueError as ve:
    print(ve)
else:
    print(d)


l = [45,89,9]
se = (1,1,6,7)
di = {'r': 7,'a': 4,'i': 2}
tup = {'t','u','e'}
print(type(l))
print(type(se))
print(type(di))
print(type(tup))

#<class 'list'>
#<class 'tuple'>
#<class 'dict'>
#<class 'set'>








    
    

    
  

