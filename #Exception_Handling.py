#Exception_Handling
print("---------------------------------")
from abc import ABC 

class animal(ABC):
    pass


# Conditional example
num = int(input("Enter number between 1 and 10: "))
if 1 <= num <= 10:
    print("Valid number")
else:
    print("Invalid number")

# Exception handling example
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid integer!")


#Without exception handling, runtime errors cause the program to terminate abruptly, producing no useful output and poor user experience. Exception handling allows the program to:

#Continue or terminate gracefully.
#Provide meaningful error messages.
#Help the programmer identify and solve bugs early.
#This mechanism ensures that the program doesn't halt at unexpected locations and informs the user of the problem precisely.


print("Errors can be broadly categorized into three types:")

#Syntactical Errors: Errors in code syntax; detected by the interpreter or compiler and prevent the program from running.
#
#Example: Missing colon, indentation errors, wrong keywords.
#Semantic Errors: These relate to the meaning of the code and usually cause logical issues, like wrong loops or conditions.
#
#Example: Looping incorrect number of times causing wrong output.
#Logical Errors: Errors in the program logic or operations causing incorrect behavior even if code runs without syntax error.
#
#Example: Division by zero, file not found for a specified path.
#Identifying and fixing these errors early makes development efficient.

try:
    inp = int(input("pick a number:"))
    if inp not in range(1,11):
        raise ValueError("inp out of range")
except ValueError as e:
    print(f'error:{e}')
else:
    print(inp)

    

try:
    name = str(input("type the administrator:"))
    if name == "raunakghoshorg@outlook.com":
        print("you have the access")
    else:
        raise ValueError("incorrect format or user")
except ValueError as v:
    print(f'RaisedError is:{v}')



#Sometimes, we want to manually trigger an exception when certain conditions occur. Python provides the raise keyword to throw exceptions explicitly.
#
#In the example below, if the user inputs a number outside the accepted range, a ValueError is raised with a custom message.    
print("--------------------------------------")

print('Handling multiple exceptions')

#A single try block can raise multiple different exceptions. We can handle each exception specifically by using multiple except blocks.
#
#Example: Handling ValueError and ZeroDivisionError separately:

try:
     divisor = int(input("type a number"))
     devider = int(input("type another number"))
     result = devider/divisor
except ValueError:
    print("Enter a correct format")
except ZeroDivisionError:
    print("divisor should not be zero")

else:
    print(result)
print("---------------------------------------------")
print("Generic Exception")

try:
    deno = int(input("provide a number"))
    result = 10/deno
except Exception as e: 
    print("something went wrong",e)
else:
    print(result)


#If you do not know the possible exceptions or want to catch all exceptions, you can catch the base Exception class. This is a generic catch-all handler but less informative.
#
#Use generic except blocks sparingly, ideally with logging or printing the exception message.    

print("----------------------------")

print("User defined exception")

try:
    DOB = int(input("Provide your DOB"))
    job_life = (60-(2025-DOB))
except Exception as e:
    print("The format is incorrect:",e)
else:
    print(job_life)
    


print("-------------------------------------------")

#You can create your own exceptions by subclassing the built-in Exception class. This is useful for specific application requirements.
#
#Steps to create a custom exception:
#
#Define a new class that inherits from Exception.
#Raise this custom exception explicitly using raise.
#Catch the custom exception in an except block.
class negetivenumbererror(Exception):
    pass

try:
    div = int(input("choose a num"))
    result = 10/div
    if div <= 0:
        raise negetivenumbererror("choosen number is incorrect")
except negetivenumbererror as ne:
    print(f'ErrorDetail:{ne}')
else:
    print(result)






