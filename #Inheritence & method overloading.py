#Inheritence & method overloading

#class Animal:
#    def __init__(self,name):
#        self.name = name
#
#    def speak(self):
#        print(self.name,"Some sound")
#
#
#
#class cat(Animal):
#    def speak(self):
#        print(self.name,"Meow")
#
#
#Cat = cat("Tom")
#Cat.speak()

#class flyer:
#    def fly(self):
#        print("flying high")
#
#
#class swimmer:
#    def swim(self):
#        print("swimming in water")
#
#class duck(flyer, swimmer):
#    def quack(self):
#        print("quack quack")
#
#
#
#duck1 = duck()
#duck1.fly() 
#duck1.swim()
#duck1.quack()

#class person:
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
#
#    def display_info(self):
#        print(self.name, self.age)
#
#
#class employee(person):
#    def __init__(self, name, age,salary):
#        super().__init__(name, age)
#        self.salary = salary
#
#    def display_info(self):
#        print(self.name, self.age, self.salary)
#
#
#
#class developer(employee):
#    def __init__(self, name, age, salary, programming_language):
#        super().__init__(name, age, salary)
#        self.programming_language = programming_language
#
#    def display_info(self):
#        print(self.name, self.age, self.salary, self.programming_language)
#
#
#
#dev1 = developer("Alice", 30, 80000, "Python")
#dev1.display_info()  


#class employee:
#    def __init__(self,namme,salary):
#        self.name = namme
#        self.salary = salary
#
#    def display_info(self):
#        print(self.name, self.salary)
#
#
#class developer(employee):
#    def __init__(self, namme, salary, programming_language):
#        super().__init__(namme, salary)
#        self.programming_language = programming_language
#
#    def display_info(self):
#        print(self.name, self.salary, self.programming_language)
#
#class manager(employee):
#    def __init__(self, namme, salary,department):
#        super().__init__(namme, salary)   
#        self.department = department
#
#    def display_info(self):
#        print(self.name, self.salary, self.department)
#
#
#manager1 = manager("Bob", 90000, "Sales")
#manager1.display_info()
#developer1 = developer("Alice", 80000, "Python")
#developer1.display_info()


class logger:
    def __init__(self):
        pass
    def log(message):
        print(f"Log: {message}")

class advancedlogger(logger):
    def log(message):
        return super().log()
        print("Advanced Logging enable")


log1 = logger()
log1.log(message = "This is a basic log message")














    
    
              
        






        



        
        