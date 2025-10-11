#Assignment7
import csv
import json

 
product = [['Name','Price'],
            ['Laptop',1000],
            ['Mouse',20],
            ['Keyboard',50]]


with open('product.csv','w',newline='') as f:
    fwr = csv.writer(f)
    fwr.writerow(product)

print('csv created successfully')

products = [
  {"Name": "Laptop", "Price": 1000},
  {"Name": "Mouse", "Price": 20},
  {"Name": "Keyboard", "Price": 50}
]

with open('product.json','w') as fj:
    json.dump(products , fj)

print('json created successfully')

with open('product.csv','r') as fcs:
    rd = csv.reader(fcs)
    for row in rd:
        print('Total no of products:',len(row)-1)
        print(row[1])
        
with open('product.json','r') as jf:
    fpro = json.load(jf)
    c = 0
    print('toatal no of products:',len(fpro))
    for i in range(len(fpro)):
        c += fpro[i]['Price']
        avg = c/(len(fpro))
    print('Avarage price in json:',avg)    
            


           
           
