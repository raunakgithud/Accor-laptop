#Brute_force

#When you write Python code in a file like code.py and run it, internally multiple steps occur to translate the high-level Python code to an executable form that the machine (computer) can understand and run.
#
#High-Level Code (source code): The Python .py file contains human-readable code.
#Compilation to Bytecode: When you run the .py file, Python compiles it into bytecode, an intermediate code that is a lower-level and platform-independent representation of your source code. This bytecode is saved in the __pycache__ folder in files ending with .pyc.
#Python Virtual Machine (PVM): Python uses a virtual machine to execute this bytecode. The PVM reads the bytecode line-by-line and executes the corresponding machine-level instructions.
#This process makes Python both compiled and interpreted language: it compiles the source code to bytecode (compilation phase), then interprets the bytecode (interpretation phase) to execute the program.

print("--------------------")

print("Brute Force Algorithm")

#Example: Running python code.py compiles code.py into __pycache__/code.cpython-xx.pyc (bytecode) and the PVM executes this bytecode to produce output.

print("------------")

#Compilation Time:
#
#During compilation, Python checks for compile-time errors such as syntax errors and type errors (e.g., adding integer to string), and compiles source code to bytecode.
#The compiler maps the required libraries and ensures the code is syntactically and semantically correct before producing executable bytecode.
#Run Time:
#
#When the program runs, the Python Virtual Machine executes the bytecode line-by-line.
#Run-time errors occur here, including logical errors that can't be detected during compile time, such as accessing an index out of range or improper file/network access.

#When Python compiles a .py file, it generates a bytecode file .pyc which is saved inside the __pycache__ folder. This bytecode file contains the compiled version of your code and is machine independent.
#
#The __pycache__ folder is for Python internal use and should not be modified by the user.
#The naming of the .pyc files includes details of the Python version used, e.g., module.cpython-39.pyc.
#Python does not generate bytecode when the program is a single file with no imports, because there’s no need for optimizations or re-use.
#Example: If you have a file example.py, after running it, you'll see __pycache__/example.cpython-39.pyc (Python 3.9) created.
print("------------")

#Python is often called an interpreted language but internally it compiles source code to bytecode first.
#
#Compiler: Converts source code to bytecode (.pyc files).
#Interpreter (PVM): Executes bytecode by processing instructions line-by-line at run time.
#Unlike compiler-based languages like C++, where the compiler expands all function definitions and performs thorough checks before execution, Python’s compiler only checks the presence of functions/methods and doesn’t inline function definitions during compilation.
#
#This leads to late binding, where the method to execute is decided at run time, as opposed to early binding in compiler-based languages where calling method definitions are resolved at compile time.

print("------------")

#Early Binding:
#
#Compiler-based languages resolve function/method calls and expand the definitions during compilation.
#Time-consuming at compile time but execution is faster.
#Late Binding (Python):
#
#Python's compiler does not expand the function definitions.
#The exact method to invoke is decided at runtime based on the Method Resolution Order (MRO).
#Allows flexibility such as method overriding and polymorphism.
#Example of Late Binding in Python:

my_list = [5, 10, 15, 20]
print(my_list[1:3])
my_list

my_list1 = [1, 2, 3, 4, 5]
result = [x * 2 for x in my_list1 if x % 2 == 0]
print(result)


st = " string "
st.strip()

print(st.strip())  # Output: "string"

print("Hello" * 3)


x = [1, 2, 3]
y = x
y.append(4)
print(x)






l = [1, 2, 3, 4, 5]
l.pop(l.index(3))
#l.remove(index=2)

sr = "raunak"
sl = list(sr)
srr = ''.join(sl)
print(srr)  # Output: "raunak"
print("------------")

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

for i in range(len(l2)):
    l1.append(l2[i])



print(l1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s_r = "raunak"

d = {}
for i in range(len(s_r)):
    if s_r[i] not in d:
        d[s_r[i]] = 1
    else:
        d[s_r[i]] += 1

for key in d:
    print(f"{key}-{d[key]}" ,end =" ")


    

print(d)

arr = [1, 2, 3, 4, 5]
sum(arr)  # Output: 15
print(sum(arr))
c = 0
for i in range(len(arr)):
    if(c+arr[i])%2 == 0:
        print(arr[i], end=" ")
        




