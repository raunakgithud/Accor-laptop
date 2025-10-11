#assignment2

with open('info1.txt','w') as f:
    f.write('name:alice\n')
    f.write('age:45\n')
print("Data saved successfully")

with open('info1.txt','r') as f1:
    context = f1.read()
    print(context)



import csv
data =[['Name','Position','Salary'],
       ['Alice','Engineer','70000'],
       ['Bob','Designer','65000'],
       ['Charlie','Manager','80000']]

with open('employees.csv','w',newline='') as file:
    filewrite = csv.writer(file)
    filewrite.writerow(data)

with open('employees.csv','r') as fl1:
    fileread = csv.reader(fl1)
    for row in fileread:
        print(row)


with open('employees.csv','r') as fapp:
    fapreader = csv.reader(fapp)
    fl = list(fapreader)
    fl.append(['Diana','Data Scientist','75000'])


with open('employees.csv','r') as fi:
    fieread = csv.reader(fi)
    for row in fieread:
        print(row)




