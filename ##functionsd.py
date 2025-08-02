##functionsd


# class is the blue print
# instanses created inside a class in called object(function)
# 
class example:
    pass

class pancake:
    ingredient = 'flour'
    def make():
        print('pancake')






class car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year


car1 = car('toyota','innova',2021)
car2 = car('honda','i20',2023)

print(car1)
print(car2)

#<__main__.car object at 07840169F0>
#<__main__.car object at 0x000001B784016990>

#object = state + behaviour + identity

#state -- data object
#behaviour --- method or function

#identity--memorylocation '0x000001B784016990'

class bycycle:
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed
    def ride(self):
        print(f"riding a bycyle{self.color} with a speed {self.speed} kmh")



bike1 = bycycle('blue',20)
bike2 = bycycle('black',15)

bike1.ride();
bike2.ride();


class student:
    def __init__(self,name):
        self.name = name


    def introduction(self):
        print(f"my name is{self.name}")


print(student)

s1 = student('joy')
s2 = student('omprakash')
s3 = student('Omkar')

print(s1)
print(s2)
print(s3)

s1.introduction()
s2.introduction()
s3.introduction()
 
print(s1.name)
print(s2.name)
print(s3.name)

#Non parameterized function 

class lamp:
    def __init__(self):
        self.color = 'red'
        self.switch = 'on'

    def switchstate(self):
        self.switch = 'off'
        print(f'buttom {self.color} is {self.switch}')

l1 = lamp()

print(l1.color,l1.switch)

l1.switchstate()

# inside a class we have to use self to access any 
# data or function
#out side a class we have to create an instance 
#like l1 of lamp






        





    


        
