#######List and string##################

rahul_friend = 24

## List

rahul_friend  = [24,21,23,20,21]

print(rahul_friend)

store = []

store = [1,3,5,'sam',True,[2,3]]

print(store)

print(store[3])

print(store[4])

print(store[5])  ##### indexing ptoperty 

##### Mutable property ###########
store.append([True,False,['sam'],0]) 

print(store)

store.remove('sam')  ### deleting elements

print(store)


store[0] = '1'

print(store);

# indexing allows access each element while slicing allows to subset ##

print(store[0:3])  ## slicing

##### strings in python #########

Name = 'Masai'

print(Name);

print(Name[1]);  ###  indexing in string

print(Name[0:4]) ### slicing property in strings

#  Name.append(q) # AttributeError: 'str' object has no attribute 'append'
# strings are immutable cant append cant remove


### converting Strings to list  #####

## use split() to convrt 

words = 'change Happens'

print(words)

words.split()
print(words)

words = 'change Happens'.split()  # converted to list

print(words)   

words[1] = 'H'

print(words)

### convertinga list to string using join() #####

Words = ''.join(words)

print(Words); #converted

#### updating strings

string = 'raunak'

print(string)

my_list = list(string) # convert string to list

print(my_list)

my_list[2] = 'o' # updated list

print(my_list)

string_back = ''.join(my_list)  # convert back to string

print(string_back);







