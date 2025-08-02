#sets and tuple


####______mutable ---- Imutable---##### List mutable ###string immutable

#sets  
# unordered   no indexing  

# store unique value

# Immutable

s = {1,2,3,3,5}   #stores unique value

print(s)

# check element

check_2 = 3 in s

print(check_2)

check_7 = 7 in s

print(check_7)


# converting a list to set

lis =[1,1,2,2,3,5,6,1]


print(lis)

set_lis = set(lis)   # set() to convert list 

print(set_lis)

se = set()

print(type(se))   # Empty set

#adding element

se.add(12)

print(se)  # can add value but cant update immutable


new_s = set(('green','red','white'))

print(new_s)

type(new_s)

print(type(new_s))


new_s1 = set(['green','red','white'])

print(new_s1)

print(type(new_s1))

# two ways to createa set set(())  set([])

#######-----------------------------------------------


t = {'apple','banana','lichi','graps'}

print(t)

t.add('kiwi')

print(t)
### add list to set

l = ['onion' ,'tomato' ]

print(l)

print(type(l))   # l is a list
print(t)
print(type(t))  # t is a set

t.update(l) # can update list into set

print(t)

#remove operation  remove()  discard()

t.remove('graps')    # throws error if element is not there in set
t.discard('banana')  # doesn't throw error

print(t)

#####  Tuple ##########

# sibling of list but  different in a way # immutable no add()

# doesnt allow addition deletion replacement 
# indexing and slicing and marging prperty

tup = (1,2,3)

print(tup)
print(type(tup))

# merging

new_tup = (4,5,6)

tup1 = tup + new_tup

print(tup1)

print(type(tup1))

#############################

my_set = {1,2,3}

print(my_set)

my_set.add(4)

print(my_set)

my_set.remove(2) 

print(my_set)

####MY_set cant be updated as its immutable

tupp = (1,'apple',9,0)   #new tupple has been created 

print(tupp)

print(tupp[2])

print(tupp[1])  #indexing supported 

# data type shouldnot be uniqe

type(tupp)

print(type(tupp))

#converting between lists and sets

my_list = [1,2,2,4,5,6]

print(my_list)

print(type(my_list))

m_set = set([1,4,4,6,6,7,0])

print(m_set)

print(type(m_set))


m_set1 = set(my_list)

print(m_set1)

print(type(m_set1))

m_list = list(m_set1)

print(m_list)

print(type(m_list))

###################################

try:
    my_set = {1, 2, ['Python']}
except TypeError as e:
    print(e)






l1 = ['onion', 'tamoto']

print(len(l1))
list = ["!","@","#","$","%","^","&","*" ]
i = len(list)
N = 10 
j = 0
while(N < 25) & (j <= i-1 ):
    print(list[j],"-",N)
    N = N+2
    j = j+1

























