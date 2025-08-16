#Dictionary_concept

print("hello dictonary")

d = {
    "maths" : 100,
    "English" : 76,
    "Bengali" : 89,
    "physics": 91,
    "chemistry":96
}

print(d["Bengali"])

#Accessing values:
#
#Use square brackets and specify the key.
#Accessing a non-existent key causes a KeyError.
#Adding or updating entries:
#
#Assign a value to a key using dict[key] = value.
#Use the update() method to add multiple pairs.

d.update({"math": 100})

d["Bengali"] = 76

print(d)
print("----------------")

#Dictionary keys and iterations 

dic = {"amy": 36,"john": 27, "shreya": 40,"Dilip": 34}
print(dic)

dic["amy"] = 63
print(dic)
print(dic.keys())
print(dic.values())
for name in dic.keys():
    print(f"{name} is :{dic[name]}")

#You can retrieve all keys from a dictionary using the built-in method keys(). Iterating through a 
#dictionary using a for loop iterates over its keys by default.


print("-----------------------")

#You can delete a key-value pair from a dictionary using the del statement with the key.
#
#len(dictionary) returns the number of key-value pairs.
#clear() method empties the dictionary.

age = {"raunak": 35,"bhanu":65,"sri":76}
print(age)

del age["raunak"]
print(age)
age.update({"samrat": 54})

print(age)

age['gouri'] = 23
print(age)
age.clear()


print("--------------------------")



