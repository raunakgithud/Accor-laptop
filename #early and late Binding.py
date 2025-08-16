#early and late Binding
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Barks")

class Cat(Animal):
    def speak(self):
        print("Meows")

def make_sound(animal):
    animal.speak()

make_sound(Dog())  # Output: Barks
make_sound(Cat())  # Output: Meows


class human:
    def name(self):
        print("name")

class raunak(human):
    def name(self):
        print("raunak")

class primat(human):
    def name(self):
        print("pritam")

def humanclasification(person):
    person.name()

humanclasification(raunak())
humanclasification(primat())

# calling a class or object with a function//global

souman = human()
humanclasification(souman)
#Interpreted languages like Python translate code line-by-line 
#at runtime allowing late binding, while compiled languages 
#translate entire code before execution enabling early binding.

print("----------------------------")

#Method resolution order

print(human.mro)
print(Cat.mro)

print("----------------------------------")
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.show()

