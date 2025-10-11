#assignment3

import csv
data =[['Name','Position','Salary'],
       ['Alice','Engineer',70000],
       ['Bob','Designer',65000],
       ['Charlie','Manager',80000]]

with open('employees.csv','w',newline='') as file:
    filewrite = csv.writer(file)
    filewrite.writerow(data)

with open('employees.csv','r') as fl1:
    fileread = csv.reader(fl1)
    for row in fileread:
        print(row)

app = ['Diana','Data Scientist',75000]
with open('employees.csv','r') as fapp:
    fapreader = csv.reader(fapp)
    fl = list(fapreader)
    fl.append(app)


with open('employees.csv','r') as fi:
    fieread = csv.reader(fi)
    for row in fieread:
        print(row)

        
