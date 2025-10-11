#Assignment4

import csv

data = [['Name','Position','Salary'],
        ['Alice','Engineer',70000],
        ['Bob','Designer',65000],
        ['Charlie','Manager',80000]]

print(data)

with open('employees.csv','w',newline='') as f:
    fwrit = csv.writer(f)
    fwrit.writerow(data)

print('employees.csv created successfully')
app = ['Diana','Data Scientist',75000]
with open('employees.csv','r') as fr:
    fread = csv.reader(fr)
    fl = list(fread)
    fl.append(app)
    print(fl)

with open('employees.csv','w',newline='') as newf:
    newfread = csv.writer(newf)
    newfread.writerow(fl)

with open('employees.csv','r') as newfl:
    newflread = csv.reader(newfl)
    for row in newflread:
        print(row)

fl = [ row for row in fl if row[2] > 7000 ]


with open('employees.csv','w',newline='') as cond:
    newcond = csv.writer(cond)
    newcond.writerow(fl)












