#computational_complexities

#P vs NP problems

print('P vs NP Problems')
# Computational problem map i/p to the o/p
#a subset of computational problems are decision problems 
#boolean o/p 'yes' 
#or 'No'
#complexity classes:


#Different complexity classes group problems based on the time complexity of their known algorithms.
#
#P class (Polynomial time): This contains all problems that can be solved in polynomial time, i.e., in time complexity O(n^k) for some constant k. Problems here are considered efficiently solvable.
#
#EXP class (Exponential time): Contains problems solvable in exponential time, like O(2^(n^c)) for some constant c. These problems are harder to solve than those in P.
#
#R class (Decidable or Recursive problems): These are problems that can be solved in finite time by some algorithm, possibly even more than exponential time.
#
#The sets relate as: P ⊆ EXP ⊆ R

print('===================================')
#cycle detection in a graph


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': ['B']  # Back edge, cycle here
}

print(graph)

def dfs(graph,node):
    visited = set()
    stack = []
    if node in stack:
        return True
    if node in visited:
        return False
    stack.append(node)
    for nei in graph[node]:
        if nei not in visited:
            return True
        stack.remove(node)
        visited.add(node)
        return False
    
print(dfs(graph,'A'))

#relation between P and NP clases


s = 'zoomsessionmooz'

#left = 0 
#right = len(s) -1 
#visited = set()
#list = []
#ln = 0
#
#visited.add(s[left])
#print(list)
#print(visited)
#while left < right:
#    list.append(s[left])
#    left += 1
#    for value in list:
#        if value not in visited:
#            visited.add(value)
#            maxln = max(ln,len(visited))
#            minsize = min(len(s)-1,len(list)-1)
#print(minsize)            



def maxsubstr(s):
    left = 0 
    right = len(s) -1 
    visited = set()
    list = []
    ln = 0
    visited.add(s[left])
    while left < right:
        list.append(s[left])
        left += 1
        for value in list:
            if value not in visited:
                visited.add(value)
                maxln = max(ln,len(visited))
                minsize = min(len(s)-1,len(list)-1)
    return minsize

s = 'zoomsessionmooz'
print(maxsubstr(s))

#{'z': 2, 'o': 5, 'm': 2, 's': 3, 'e': 1, 'i': 1, 'n': 1}




def noOfedible(plants,edible):
    count = 0
    for value in plants:
        if value in edible:
            count+=1
    return count
edible = 'xY'
plants = 'AYxxXY'
print(noOfedible(plants,edible))



#str, N
print('--------------------')

#def maxcons(str):
#    vowel = 'aeiou'
#    setv = set(vowel)
#    left = 0
#    right = len(str)-1 
#    
#    while left < right:
#        sum = 0
#        if str[left] not in setv:
#            currentsum = sum + 1
#        else:
#            currentsum = sum
#        left += 1
#        maxsum = max(sum,currentsum)
#    return maxsum       
str = 'abced'

#print(maxcons(str)) 
vowel = 'aeiou'

left = 0
#print(str[left])
right = len(str) - 1

sum = 0
while left < right:
    sum_values = []
    if str[left] not in vowel:
        sum += 1
        

    else:
        sum = 0
    sum_values.append(sum)
        
    left += 1
    
    print(max(sum_values))


def maxcons(str):
    vowel = 'aeiou'
    left = 0
    right = len(str) - 1
    sum = 0
    while left < right:
        sum_values = []
        sum_values.append(sum)
        if str[left] not in vowel:
            sum += 1
        else:
            sum = 0
        
        left += 1
    return max(sum_values)      
      
arr = [1, 2, 10]

n = len(arr)
count = 0
left = 0
right = 0
n = len(arr)
sub = []
for left in range(n+1):
    for right in range(n+1):
        if left < right:
            sub = arr[left:right]
            if 10 in sub:
                count += 1
print(count)   

def maxcout(arr,target):
    n = len(arr)
    left = 0
    right = 0 
    sub = []
    for left in range(n+1):
        for right in range(n+1):
            if left < right:
                sub = arr[left:right]
                if target in sub:
                    count += 1
    return count

array = [3, 0, 6, 2, 7]
target = 9
newcount = 0
pointer1 = 0 
while pointer1 < len(array):
    pointer2 = pointer1 + 1
    while pointer2 < len(array):
        if array[pointer1] + array[pointer2] == target:
            newcount +=1 
        pointer2 += 1
    pointer1 += 1 

print(newcount)     

def sumcount(array , target):
    newcount = 0
    pointer1 = 0 
    while pointer1 < len(array):
        pointer2 = pointer1 + 1
        while pointer2 < len(array):
            if array[pointer1] + array[pointer2] == target:
                newcount +=1 
            pointer2 += 1
        pointer1 += 1 
    return newcount
print(sumcount([3, 0, 6, 2, 7],9))

def two_sum(n,arr,target):
    left = 0
    right = n-1
    
    while left < right:
        sum = arr[left] + arr[right]
        result = []
        if sum == target:
            return left,right
        elif sum > target:
            right -= 1
        else:
            left += 1
    return -1
print(two_sum(4,[2 ,7, 11, 15],9))      
print('-----------------------------')  

l = [2 ,7, 11, 15]
t = 9
n = 4
left = 0
right = n-1


    

    












        


       
        



    

#print(newcount)


              
              


            
               

      
               
       





    
      





    
            
          



         
    
    

        

#print(current)         
#vow = 'abcde'
#l = list(vow)
#print(l)                   

#def maxconsonent(str):
#    vowel = 'aeiou'
#    left = 0
#    right = len(str) - 1
#    sum = 0
#    while left < right:
#        if str[left] not in vowel:
#            current =sum + 1
#        else:
#            current = sum
#            sum = 0
#        left += 1
#    return max(sum,current)
#print(maxconsonent(str = 'abced'))        





    




            


                
    
        







