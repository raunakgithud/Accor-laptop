#dictionary

lst = [1, 2, 3, 4]  
lst.insert(2, 5)  
print(lst)  


lst = [3, 1, 4, 2]  
lst.sort()  
print(lst)  


lst1 = [1, 2, 3, 4, 5]  
print(lst1[-3:])  


###########################################

my_dic = {}

print(my_dic)

print(type(my_dic))

my_dic = {
    'name' : 'raunak',
    'branch' : 'electorins',
    'city' : 'kolkta'

}

print(my_dic)

d = {
    "name" : ['akshay','adi','dixit'],
    "age": [30,32,34],
    "income" : ['50k','45k','70k']

}

print(d)

print(d['name'])

print(len(d['name']))

print(type(d['name']))

print(d['name'][len(d['name'])-1])  # print(d['name'][2])  


print(len(d['name'])-1)


# another method to introduce a dictionary is

my_dict1 = dict({1:'python',2: 'java',3: 'csc',4: 'perl'})

print(my_dict1)

print(type(my_dict1))


# to access data we use  key values 

print(my_dict1[2])

#using get() func

print(d)

age = d.get('age')

print(age)

name1 = d.get('name','not found')

print(name1)  # The get method additionally allows you to provide a default value if the key is not found.


# adding or updating data

D = dict({
    'name' : 'adit',
    'age': 43 ,
    'city' : 'kolkta'
})

print(D)
print(type(D))

print(D['age'])

D['age'] = 34  # updating value

print(D)

####

#Removing data from dictionary

exam_d = dict({
    'name' : 'aditya',
    'age': 36,
    'designation' : 'analyst',
    'city' : 'Mumbai',
    'company': 'cts'
})


print(exam_d);

exam_d.pop('age') # to delete a perticular key value

print(exam_d)

# {'name': 'aditya', 'designation': 'analyst', 'city': 'Mumbai', 'company': 'cts'}

exam_d.popitem() # to delete last inserted value

print(exam_d)

# {'name': 'aditya', 'designation': 'analyst', 'city': 'Mumbai'}

exam_d.clear()  # to clear all the values in the dictionary

print(exam_d)

# {}

car_dict = {
    'brand' : 'ford',
    'city' : 'pune',
    'model' : 'fiesta',
    'year' : 1988,
    'year' : 2005,               # duplicate keys are not allowed
    'price' : '30lac',
    'type' : 'petrol'

}

print(car_dict)


car_dict.get('Model' , 'key not found')

print(car_dict.get('Model' , 'key not found'))

# iterating through a dictionary

#key

for i in car_dict.keys():
    print(i)

#value

for k in car_dict.values():
    print(k)

#key , value

for j in car_dict.items():
    print(j)


type(('a','b','c'))

print(type(('a','b','c')))



#dictionary
# dulicate keys are not allowed 
# duplicate values are allowed 

print(car_dict)

for i in car_dict:
    print(i,car_dict[i])
    print('nex pair')





################################################


guy = {
     'name':'papai',
     'age': 23
 }  


place ={
    'age' : 34,
    'state' : 'andhra'
}

guy.update(place)

print(guy)










    








 






