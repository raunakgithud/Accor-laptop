#strings_problem#

d = {}

print(d)

d[0] = 1
print(d)

d[0] = 'somevalue'
print(d)

#Problem 4: Find the Most Frequent Character

Input =  "success"

N = len(Input)

d1 = {}
c = 0 

for i in range(N):
    d1[Input[i]] = c
    
  
    
print(d1)

print(type(d1))


for i in range(N):
    if Input[i] in d1:
        d1[Input[i]] = d1[Input[i]] + 1
    
 
 

print(d1)

M = len(d1)

#print(M)
l = 0
for j in d1.keys():
    if (d1[j]>l):
        l = d1[j]
        print(f"the most frequent key id {j}")

##################













    
 