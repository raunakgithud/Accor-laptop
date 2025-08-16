#Interfaces, Multiple Inheritance, and Early/Late Binding in Python II
print("--------------------")

from abc import ABC , abstractclassmethod
class animal(ABC):
    @abstractclassmethod
    def speak(self):
        pass



#Abstract Base Classes (ABC) are used to enforce a certain 
#uniformity among child classes by requiring them to 
#implement certain abstract methods. The ABC is declared 
#by inheriting from ABC module and using the @abstractmethod
#decorator for defining abstract methods inside the class.


#Abstract methods are declared in the abstract base class but 
#are not implemented there. They must be implemented in the 
#child classes.
#Concrete methods are methods defined in the abstract base 
#class and can optionally be overridden by child classes.


class cat(animal):
    def speak(self):
        print("meow")

class dog(animal):
    def speak(self):
        print("bark")


tom = cat()
tom.speak()
john = dog()
john.speak()
print("------------------")

#interface in python 

#if an abstract class hollds only a abstract method and no
#concrete method is called an interface
#see below example

from abc import ABC, abstractclassmethod

class human(ABC):              # interface
    @abstractclassmethod
    def identity(self):
        pass

from abc import ABC,abstractclassmethod

class vehicle(ABC):             #not an interface   (abstract base class)
    @abstractclassmethod
    def type(self):
        pass
    def number():               #concrete method
        print("the no of the vehicle written in no. plate")



#An interface in Python can be considered as a special form 
# of abstract base class where all methods are abstract 
# (i.e., no concrete methods at all). 
# The interface defines what methods a class should implement 
# but provides no implementation.   

#No concrete method in the interface.
#Child classes are responsible for implementing all abstract methods.
#It's useful when there are no common implementations but common method signatures expected. 

#Abstract Base Class (ABC):
#
#Can have both abstract methods and concrete methods.
#Used when some common functionality is shared.
#Forces child classes to implement only abstract methods.
#Instantiation of ABC is not allowed.
#Interface:
#
#All methods are abstract.
#Used when there's no common implementation but a requirement for common method signatures.
#Gives full freedom to child classes on implementation.
#Mostly used in APIs and software development for consistency.
#Regular Class:
#
#Complete implementation.
#Can be instantiated directly.

#meta class are the classes which defines the behaviour of
#other classes

print("-----------------------------")

#method overloading

#Method Overloading refers to having multiple methods with the same name but different signatures (parameters). In statically typed languages like Java or C++, this is supported natively.

#However, Python does not support traditional method 
#overloading, since the last method defined with a particular 
#name overrides previous definitions.


from abc import ABC, abstractclassmethod

class animal(ABC):
    @abstractclassmethod
    def name(self):
        pass
    def speak(self):
        pass



class pig(animal):
    def name(self):
        print("this is a pig")
    def speak(self):
        print("chihua")


tumba = pig()
print(tumba.name())

tumba.speak()

class curtesy(ABC):
    def greet(self,name):
        pass


class hello(curtesy):
    def greet(self, name):
        self.Name = name
        if name:
            print(f"hello {self.Name}")
        else:
            print("hello")

Hel = hello()
#Hel.greet()
Hel.greet("Preet")

class myclass:
    def sum(self,*args):
        return sum(args)

s = myclass()
print(s.sum(10,20,60,40))




print("----------------------------")

#method overridding


#Method Overriding allows a child class to provide a 
#specific implementation for a method already defined 
#in its parent class.
#
#When the method is called on an object of the child class, 
#the overriding method of the child class is executed.

#If you call a method from a parent class object, 
#parent class version runs.
#If called from child class object, child class version runs.
#This is essential for polymorphism.

#changing a method in some other class or child class

class student:
    def speak(self,name):
        self.Name = name
    def now(self):
        print(self.Name)    

class standard(student):
    def speak(self,no):
        print(f"in {no} class")


raunak = student()
pritam = standard()
raunak.speak("raunak")
raunak.now()
pritam.speak(7)
#pritam.now()
pritam.speak(9)
raunak.speak("Manik")
raunak.now()

print("------------------------------------")

#Binding refers to linking a method call to the method body.

class aminal:
    def say(self):
        print("speak...")

class cat(animal):
    def say(self):
        print("meow")
class dog(animal):
    def say(self):
        
        print("bark")

def speakmethod(Animal):
    Animal.say()
    

#tom = cat()
#speakmethod(cat()) 
#speakmethod(dog())







        







    
        
















