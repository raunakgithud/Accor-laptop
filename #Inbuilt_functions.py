#Inbuilt_functions

#Inbuilt functions are predefined functions in Python that perform common tasks. These functions come ready to use, and they help perform basic operations such as printing output, taking input, or checking data types.
#
#Some broad categories of inbuilt functions discussed are:
#
#Mathematical Functions
#String Functions (Methods)
#List Functions (Methods)
#General Utility Functions
#Functions are recognized by their name followed by parentheses, optionally with arguments inside the parentheses. For example, abs(-5) calls the absolute value function with -5 as an argument.


print(abs(-7))
print(pow(6,7))

#String functions are also called methods because they are defined inside the string class. They operate on string objects and can be called using the dot . operator.
#
#Common string methods:
#
#len(str): Returns the length of the string.
#str.upper(): Converts all characters in the string to uppercase.
#str.replace(old, new): Replaces occurrences of old substring with new.

s = "hello"

print(len(s))
print(s.upper())
print(s.replace("l", "x"))

print(round(22.7))

x = 34
print(type(x))
print(isinstance(x,str))

print(isinstance(x,int))
print(isinstance(x,float))

print(isinstance(x,object))

if isinstance(x,int):
    print(f"{x} is an integer")
else:
    print(x) #x



#Two important utility functions for dealing with types:
#
#type(obj): Returns the data type of the object obj.
#isinstance(obj, classinfo): Checks if obj is an instance of classinfo or a subclass thereof, returning True or False.
#Differences:
#
#type() returns the type itself; comparison needs to be done separately.
#isinstance() performs the type check comparison internally and gives a boolean result.


class example:
    pass

print(isinstance(example,object))
print(isinstance(example(),object))  # True, because all classes in Python inherit from object

#Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).


#Simple Inheritance: One child inherits from one parent.

class vehicle:
    def move(self):
        print("car is moving")


class car(vehicle):
    def car_function(self):
        print("gears are functioning")

honda = car()

truck = vehicle()

honda.move()
truck.move()
honda.car_function()

#Hierarchical Inheritance: One parent and multiple children inherit from it.

class shape:
    def draw(self):
        print("drawing shape")


class cir(shape):
    pass
class square(shape):
    pass

c = cir()
s = square()
c.draw()
s.draw()

#Multiple Inheritance: One child inherits from multiple parents.

class flyer:
    def fly(self):
        print("object is flying")

class swimmer:
    def swim(self):
        print("object is swimming")



class Duck(flyer,swimmer):
    pass


d = Duck()
d.fly()
d.swim()


#Multi-level Inheritance: Chain of inheritance (Grandparent -> Parent -> Child).

class plant:
    pass
class flower(plant):
    pass
class rose(flower):
    pass

#Method overriding occurs when a child class defines a method with the same name as a method in its parent class, but with a different implementation.

class human:
    def display(self):
        print("displaying human details")

class student(human):
    def display(self):
        print("displaying student details")       

class empployee(human):
    def display(self):
        print("displaying employee details")

h = human()
s = student()
e = empployee()
h.display()
s.display()
e.display()


t = "hello  world"

if(isinstance(t, str)):
    print("t is a string")
elif(type(t) == str):
        
        print("t is a string using type check")
else:
     print("t is not a string")
     
            
    




