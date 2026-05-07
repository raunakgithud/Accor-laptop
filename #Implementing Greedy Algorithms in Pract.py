#Implementing Greedy Algorithms in Practice
print('assignment')
# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT
a = [1,2,3]
n = len(a)
served = set()
timetook = {}
customer = a.pop()
print(f'customer:{customer}')
timetook[customer] = customer
served.add(customer)
for cust in a:
  if cust not in served:
    served.add(cust)
    timetook[cust] = timetook[customer] + cust
    
print(served)
print(timetook)

def happycust(a,start):
  served = set()
  served.add(start)
  timetook = {start:start}
  for customer in a:
    if customer not in served:
      served.add(customer)
      timetook[customer] = timetook[start] + customer
  happy = len(timetook)    
  return served,timetook,happy
    


print(happycust(a,1))
print(happycust(a,3))
print(happycust(a,2))


alphabets = "abcdefghijklmnopqrstuvwxyz"

def no_of_leters(str,start):
  included = set()
  included.add(start)
  x = {}
  for i in range(len(alphabets)):
    for start in str:
      if start == alphabets[i]:
        x[start] = i+1

  c = 0
  for start in x:
    if c < x[start]:
      c = x[start]      
  return c      

print(no_of_leters('a','a'))
print(no_of_leters('down','o'))


#6
#7 1 5 3 6 4
#5
#7 6 4 3 1

price = [7,1,5,3,6,4] #[7,6,4,3,1]
price2 = [7,6,4,3,1]

        


def profit(pric):
  
  t = 0
  for i in range(len(pric)):
   for j in range(len(pric)): 
    if j>i and (pric[j]-pric[i]) > t :
      
      t = (pric[j]-pric[i])
  if t > 0:
    return t
  return 0  
  
          
print(profit(price))




#5
#11 50 51 1000 2000
#3
#200 13 5000

#n = no of shops
suits = []
n = len(suits)
currency = [2000,500,200,100,50,20,10,5,2,1]
def amount(suits):
  t = 2000
  d = {}
  minimunamount = 20000
  for i in range(len(currency)):
    for price in suits:
      if price == currency[i]:
        d[price] = currency[i]
        
  for key in d:
    if minimunamount > d[key]:
      minimunamount = d[key]
  return minimunamount        
        
      #print(d)  
    
  

case1 = [11 ,50 ,51, 1000, 2000]
case2 = [200, 13, 5000]
print(amount(case1)) 
print(amount(case2)) 

  
      
  
          
    #return cost          

#array =[9, 4, 9, 7, 4]
#cost = 0
#count = 0
#d = {}
#for i in range(len(array)):
#  d[array[i]] = 0
#  #print(d)
#for i in range(len(array)):
#  for key in d:
#    if key == array[i]:
#      d[key] += 1
#      print(d)
#
#costque = {}
#for key in d:
#  costque[key] = 0
#print(costque)
parking = 1
arival = [1, 3, 5]
depurtute = [2, 6, 8]    
count = 0
n = len(arival)
i = j = 0
while i < n and j < n:
  if arival[i] <= depurtute[j]:
    count += 1
    i += 1
  else:
    count -= 1
    j += 1
print(count) 

def if_possible(arival,departure,k):
  car_count = 0
  n = len(arival)
  i = j = 0
  while i < n and j < n :
    if arival[i] <= departure[j]:
      car_count += 1
      i += 1
    else:
      car_count -= 1
      j += 1
  if car_count < k :
    return 'possible'
  return 'not possible'

arival = [1, 3, 5]
depurtute = [2, 6, 8] 
print(if_possible(arival,depurtute,1))


      

 
   
    
             

      
  


  
