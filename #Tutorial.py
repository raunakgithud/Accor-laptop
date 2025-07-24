#Tutorial

class cicle:
    pass

hero = cicle()
BSA = cicle()

class circle:
    def __init__(self,radious,color):   #radious & color are attributes
        self.R = radious
        self.Col = color

    def display(self):            #method
        print(self.R,self.Col)

        #return

    def add_radious(self,r):

        self.R += r
        print(self.R,self.Col)
        return


    

redCircle = circle(5,"red")  
yellowcircle = circle(10,"yellow")
redCircle.display()
yellowcircle.display()

yellowcircle.add_radious(5)


#Attributes are the properties or characteristics of an object/class. They hold the data specific to an instance.
#
#For example, a Circle class may have attributes radius and color.
#


#Objects (also called instances) are the actual entities created from a class.
#
#Each object can have different values for the attributes.


#Attribute: Data stored in an object to describe it, e.g., radius or color.
#Instance (Object): A specific member created from the class blueprint that has these attributes.
#Attributes define the characteristics, instances are the concrete entities having those characteristics.
            

#Methods are functions defined inside a class that describe the behaviors or actions of an object.
#
#Methods operate on the object's attributes.
#
#__init__ method is a special constructor method used to initialize objects.
#Other methods can manipulate the object's data.    

import matplotlib.pyplot as plt


#Inheritance allows one class (child or subclass) to inherit attributes and methods from another class (parent or superclass).
#
#This helps code reuse and logical hierarchy.

#class dwarCir(circle):
#    def darw(self):
#        plt.gca().add_patch(plt.Circle( self.R,self.Col))
#        plt.axis('scaled')
#        plt.show()




#greencircle = dwarCir(5,"Green")
#greencircle.darw()


class person:
    def __init__(self,name,age):
        self.N = name
        self.Ag = age
    def info(self):
        print(self.N,self.Ag)
        return


class employment(person):
        def __init__(self, name, age,profession):
            super().__init__(name, age)  
            self.prof = profession

        def info(self):
            print(self.N,self.Ag,self.prof)

        pass


raunak = person("bhutai",35)
raunak.info()


raunak_ghosh = employment("raunak",35,"engineer")
raunak_ghosh.info()

#You can add methods in classes to perform tasks, for example, drawing a circle using matplotlib.

import matplotlib.pyplot as plt
import matplotlib.patches as ptch



class drawcircle(circle):
    def draw(self):
        fig , ax = plt.subplots()
        ci_patch = ptch.Circle((0,0),self.R, color = self.Col)
        ax.add_patch(ci_patch)
        ax.set_aspect("equal","box")
        plt.xlim(-self.R*1.5,self.R*1.5)
        plt.ylim(-self.R*1.5,self.R*1.5)
        plt.show()





greencircle = drawcircle(7,"Green")
greencircle.draw()






