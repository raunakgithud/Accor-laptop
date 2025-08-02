#Function
# Inbuilt functions

class example:
    def __init__(self,name):
        self.name = name
        print(name)


s = example(name="Raunak")
s
#Code Reusability: Write once, use multiple times with different data inputs.
#Modular Programming: Break large programs into smaller, manageable parts called modules (functions).
#Code Readability and Maintainability: Easier to track, understand, and debug.
#Time Efficiency: Saves writing time since code is reused.
#Reliability: Fix errors once in function; all calls automatically use the fixed version.
#Teamwork: Multiple developers can work on separate modules (functions).
#Example: Instead of writing addition many times, define an add function and call it repeatedly.

#To define a function in Python, use the def keyword, followed by the function name, parentheses for parameters, and a colon. The body of the function is indented.        

#Functions can take inputs in the form of parameters (placeholders defined during function declaration). When you call the function, you provide arguments (actual input values), which are passed to those parameters.
#
#Parameters: Variables in the function definition.
#Arguments: Values passed to the function when called.

def add(v1, v2):
    return v1 + v2

result = add(3, 5)  # v1=3, v2=5
print(result)  # Output: 8

def add(v1, v2):
    return v1 + v2

result = add(v2=5, v1=3)  # Explicitly naming arguments
print(result)  # Output: 8

def do_math(v1, v2):
    add = v1 + v2
    subtract = v1 - v2
    multiply = v1 * v2
    return add, subtract, multiply

result = do_math(3, 5)
print(result)        # Output: (8, -2, 15)
print(result[0])     # Access addition result: 8
print(result[1])     # Access subtraction result: -2
print(result[2])     # Access multiplication result: 15

#When the number of input arguments is not fixed, Python allows 
#functions to accept a variable number of arguments by prefixing
#a parameter with an asterisk (*). 
#This collects all extra positional arguments into a tuple.

def hello_n(n, *words):
    print(f'Number of arguments: {n}')
    for word in words:
        print(word)

hello_n(3, 'apple', 'banana', 'cherry')
print("--------------------------------")
for _ in range(5):
    print('Hello')  # Prints 'Hello' 5 times
#When a loop variable is not used inside the loop, it is common
#practice in Python to use an 
#underscore _ as the variable name to indicate it is 
#intentionally unused.

