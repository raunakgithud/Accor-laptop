#CSE 101  Abstract data types in Python


#Abstract Data Types (ADTs) are theoretical models that define 
# operations for a data type but hide the implementation details. 
# In Python, ADTs like lists, tuples, sets, and dictionaries allow 
# us to use predefined operations without focusing on how these 
# operations are implemented internally.

#append(), pop(), and remove():

List = [1,2,3,4]

List.append("six")
print(List)
List.pop()
print(List)
List.remove(2)
print(List)

#Python data types can be broadly divided into 
# Primitive Data Types and 
# Abstract Data Types.

#Primitive Data Types: int, float, str, bool, and char.

#Abstract Data Types: list, tuple, set, and dictionary.

#primitive data

x = 4
print(type(x))
Name = "John"
print(type(Name))
ch = 'A'
print(type(ch))
flag = True
print(type(flag))

#Abstract data

my_list = [1,2,3,4]
my_tuple = (1,2,3,4,5)
my_set = {1,2,3,4}
my_dic = {"name": "John", "age": 30}

print(type(my_list))
print(type(my_tuple))   
print(type(my_set))
print(type(my_dic))

#A list is an ordered, mutable collection of elements in Python.
#
#Ordered means the elements maintain the order in which they are inserted.
#Mutable means you can modify the list after creation (add, remove, change elements).
#It supports indexing, slicing, and iteration.
#Allows duplicate elements.
#Common list methods include: append(), remove(), pop(), and sort().

print(my_list)
my_list.append("seven")
print(my_list)
my_list.pop()
print(my_list)
my_list.append(1)
print(my_list)
my_list.sort()
print(my_list)
my_list.remove(2)

print(my_list)
print("----------------------------")

#Assigning one list to another (e.g., l2 = l1) copies the reference, so changes to l1 reflect in l2.
#Copying with copy() method creates a new list, so changes to one list do not affect the other.

l1 = [1,2,3,4]
l2 = l1
l2.append(5)
print(l1)  
print(l2)
print("----------------------------")

l3 = l1.copy()
l3.append(6)
print(l1)
print(l2)
print(l3)
print("----------------------------")
#A tuple is an ordered but immutable collection in Python.

t1 = (1,3,4,5,8)

t2 = (1,6,4,8)

t = t1 + t2  # Concatenation
print(t1)
print(t2)
print(t)

print("-----------------------------")

#Ordered means it maintains the insertion order.
#Immutable means once created, the tuple's contents cannot be changed (no adding/removing/modifying elements).
#Supports indexing and slicing.
#Can be used as a key in dictionaries because it is hashable.
#Tuples are suitable for storing fixed data.

#Operations like addition and multiplication (repetition) are supported:


#A set is an unordered collection of unique elements in Python.
A = {1,2,3,8,9}
B = {3,4,2,7,9,10}
print(A)
print(B)
print("-----------------------------")

#Unordered means the elements are not stored in a particular sequence, so no indexing or slicing.
#Unique elements only: duplicates are automatically removed.
#Supports set operations such as union, intersection, and difference.
#Sets are efficient for membership testing and eliminating duplicates.

print(A.union(B))  # Union
print(A.intersection(B))  # Intersection
print(A.difference(B))  # Difference
print(B.difference(A))  # Difference

print(B.intersection(A))  # Intersection

print("-----------------------------")

my_d = {'A':1,'B':2,'C':3}

print(my_d)
print(my_d['A'])  # Accessing value by key
print(my_d['B'])
print(my_d.keys())  # Returns keys
print(my_d.values())  # Returns values
print(my_d.items())  # Returns key-value pairs

my_d['A'] +=1

print(my_d)
my_d['D'] = 4  # Adding a new key-value pair
print(my_d)

#Hashable means an object has a constant hash value throughout its lifetime, which implies immutability. Hashable objects can be used as keys in dictionaries and stored in sets.
#
#Mutable objects (like lists) can change, so they are non-hashable and cannot be used as dictionary keys.
#Immutable objects (like tuples, strings, numbers) are hashable.



