#control structure#

#print(int('10.5')) # throws error int convert decimal to integer


print(int(10.5))

age = 18 
if age >= 18 :
    print("eligible")
else:
    print('not eligible')



num = 5
if num > 0 :
    print('positive') 

if num < 0:
    print('negetive')

if num%2 ==0:
    print('even')
else:
    print('odd')

score = 85
if score > 90:
    print('grade A')
elif score > 80:
    print('grade B')
else:
    print('grade C')


month = 'December'
time_of_day = 'afternoon'

if month == 'December':
    if time_of_day == 'afternoon':
        print('Go outside')
    else:
        print('Stay inside')
else:
    print('Stay inside')   

############################
number = 12
if number % 2 == 0:
    if number % 3 == 0:
        print('Divisible by both 2 and 3')
    else:
        print('Divisible by 2 but not by 3')
else:
    print('Not divisible by 2')

####################################
#for variable in iterable:
    # code block          
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

###############################
for i in range(1, 7):  # from 1 up to but not including 7
    print(i)

for i in range(1,9,3):
    print(i)

#range(start, end, step) generates numbers from start to end - 1 stepping by step.

for i in range(10, 0, -2):
    print(i)

#The range() function can take up to three arguments:

#start: Starting number of the sequence (inclusive).
#stop: Stop number (exclusive).
#step: Difference between each number in the sequence.                

string = 'raunak'

list_str = list(string)
print(string)
print(list_str)

string_back = ''.join(list_str)
print(string_back)
string_slice = string[3:]
print(string_slice)
dict = {}
set_string = set(list_str)

print(set_string)
for i in range(len(string)):
    dict[list_str[i]] = 0


print(dict)
#for key in dict.keys():
 #
 #    if list[]

for i in range(len(string)):
    if list_str[i] in dict.keys():
        dict[list_str[i]] = dict[list_str[i]] + 1
        

    

print(dict)

for i in range(10,-1,-2):
    print(i)


for i in range(10,-2,2):
    print(i)


#while

count = 0
while count<5:
    print(count)
    #count = count+2
    count += 2


#Loop control statements

#continue    break

no = 0
while no < 5:
    no +=1
    if no == 3:
        break #3 will not get print

    print(no)
print("------------")
r = 0
while r < 10:
    r += 2
    if r == 4:
        continue
    print(r)


print('=========')







    









           

