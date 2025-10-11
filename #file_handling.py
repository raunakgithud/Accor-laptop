#file_handling
#D:\txt

#data
#structured data and unstructured data
import csv
 
data = [
    ['name','address','marks'],
    ['raunak','pune',100]
] 

#Files are stored within directories (folders) on drives, and their locations are specified through paths. The absolute path includes the drive name, and all directories leading to the file.
#
#For example, C:\Users\Documents\students.csv is an absolute path where:
#
#C: is the drive
#Each \ separates directory levels
#students.csv is the file name

print("-------------------------------------------------")

#Structured Data refers to data organized in a defined manner, often tabular with rows and columns like in databases or CSV files. Each row is called a record or an entry, corresponding to an entity (e.g., an employee).
#
#Unstructured Data refers to data without a predefined structure such as paragraphs, stories, or free text in TXT files. While unstructured, files do have formatting characters invisible to users (like newlines) to help understand the structure.
#
#Applications rely on delimiter characters (commas, quotes, new lines) to parse and process the data inside files.

with open('data.csv','w',newline='') as file:

    writer = csv.writer(file)
    writer.writerows(data)


print("csv created successfully")


dbcsv = [['folder','filname','date'],
         ['xl','macro.xlsx','26-07'],
         ['txt','batch.txt','28-07']]

with open('dbcsv.csv','w',newline='') as file:
    writefile = csv.writer(file)
    writefile.writerows(dbcsv)

#Here, newline='' parameter is used to prevent blank lines between rows on some platforms.
print("dbcsv created successfully")

#To read data from CSV files:
#
#Open the file in read mode ('r').
#Create a CSV reader object using csv.reader(file).
#Iterate over the reader to get each row as a list.


newdata = [["cluster","hostname","address","pakage"],
           ["DB-HOST","RWS-THW","172.45.354.01","Apache2"],
           ["DB-HOST","REW-TGH","172.45.354.02","NGINX"],
           ["DB-HOST","RTY-UYT","172.45.354.03","Apache-tomcat"]]

import csv

with open('clustr.csv','w',newline='') as csvfile:
    cluster = csv.writer(csvfile)
    cluster.writerows(newdata)

#read a csv file as below 

import csv

with open('clustr.csv','r') as csvread:
    clusterread = csv.reader(csvread)
    for row in clusterread:
        print(row)

#updating a csv file

import csv

with open('clustr.csv','r') as updatecsv:
    csvupdate = csv.reader(updatecsv)
    rows = list(csvupdate)
rows.append(["DB-HOST","REI-YTR","172.45.354.07","IIS"]) 

print("row has been updated")


datasrc = [['fileName','fileType','filemode','date'],
           ['data','csv','readwrite','10Aug'],
           ['data1','xlsx','write','08Aug'],
           ['data2','txt','read','09Aug']]

with open('filetype.csv','w',newline='') as filetype:
    filecsv = csv.writer(filetype)
    filecsv.writerows(datasrc)

print("file has been created succfully")

import csv
with open('filetype.csv','r') as readfile:
    obsreadfile = csv.reader(readfile)
    for row in obsreadfile:
        print(row)


with open('filetype.csv','r') as readfile:
    obsreadfile = csv.reader(readfile)
    totAl_row = list(obsreadfile)

totAl_row.append(['data20','batch','readwrite','12Aug'])

with open('filetype.csv','r') as readfile:
    obsreadfile = csv.reader(readfile)
    for row in obsreadfile:
        print(row)
#opening a file in different mode

with open('data.txt','w') as txtfile:
    txtfile.write("Hello world")
print("txt file has been created successfully")

#The open() function in Python allows specifying the mode in which to open a file:
#
#'r' : Read mode (default). File must exist.
#'w' : Write mode. Creates a new file or truncates existing.
#'a' : Append mode. Adds data to the end of the file.
#'x' : Exclusive creation, failing if the file already exists.
#Modes can be combined with 'b' for binary or 't' for text (default).


#read a text file 

with open('data.txt','r') as txfile:
    filecontent = txfile.read()
    count_l = filecontent.count('l')
    print(count_l)

import csv

element =['csv','csv','csv','csv']

with open('check.csv','w',newline='') as trycsv:
    writcheck = csv.writer(trycsv)
    writcheck.writerow(element)

print('created successfully')


with open('check.csv','r') as checkcsv:
    readcsv = csv.reader(checkcsv)
    for row in readcsv:
        print(row)

with open('try.txt','w') as extxt:
    extxt.write("hey raunak hows doing")

print('file created successfully')

with open('try.txt','r') as emple:
    inside = emple.read()
    count_ranak = inside.count('raunak')
print("read successfully")


try:
    with open('tr.txt','r') as readtry:
        rdcontnt = readtry.read()
except FileNotFoundError:
    print("file not found")
else:
    print("file has been read")


try:
    with open('try.txt','r') as readtry:
        rdcontnt = readtry.read()
except FileNotFoundError:
    print("file not found")
else:
    print("file has been read")





    













    









