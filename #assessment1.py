#assessment1.py

print('-----------------------------')

print("file_handing Asesment:")

print("-----------------------------")

#txt1 = "Python"
#txt2 = "File Handling"
#txt3 = "is fun!"



with open('data.txt','w',newline='') as txtdata:
    txtdata.write("Python\n")
    txtdata.write("File Handling\n")
    txtdata.write("is fun!\n")

print("file created successfully")

with open('data.txt','r') as f:
    content = f.read()
    print(content)

with open('data.txt','a') as fileAppend:
    fileAppend.write("End of file\n")
    fileAppend.close()

file = open('data.txt','r')
txts = file.read()

print(txts)



name = 'name'
age = '89'

file = open('info.txt','w')
file.write(name)
contents = file.write(age)
print(contents)



with open('info1.txt','w') as f:
    f.write('name:alice\n')
    f.write('age:45\n')
print("Data saved successfully")

with open('info1.txt','r') as f1:
    context = f1.read()
    print(context)



    


