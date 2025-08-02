#list problems#

#Problem Statement: Write a program that prompts the user to enter 5 numbers (one by one). Append each number to a list and print the final list.

list = []

element1 = input("type element1")

element2 = input("type element2")

element3 = input("type element3")

element4 = input("type element4")

list.append(element1)
list.append(element2)
list.append(element3)
list.append(element4)

print(list)

N = len(list)

d = {}
for i in range(N):
    
    if list[i] in d:
        print(d)
    else:
        d[i+1] = int(list[i])
    

print(d)

for key in d.keys():
    print(f"The element{key} is:{d[key]}")


#Finding the Maximum and Minimum Values

list1 = [10, 5, 8, 12, 3]

N1 = len(list1)

c = 0
for i in range(N):
    if(c<list1[i]):
        c = list1[i]


print(f"the maximum value is:{c}")   

m = 999
for j in range(N1):
    if(m>list1[j]):
        m = list1[j]

print(f"the minimum value is:{m}")   


###################################

#Calculate the Average

l = [4, 6, 8, 12]

n = len(l)
t = 0
for i in range(n):
    t = t + l[i]


print(f"the avarage value is:{t/n}")   


#Count Occurrences

def Occurrence(M):
    List = [1, 3, 7, 8, 3, 5, 3] #Target: 3
    
    pointer = 0
    

    for i in range(len(List)):
        if(M == List[i]):
            pointer += 1

    print(f"the number of occurence is {pointer}")


Occurrence(3)  
Occurrence(5)

#Find the Second Largest Number

def secondhighest():
    list = [4, 6, 1, 7, 9, 3]
    k = 0
    for i in range(len(list)):
        if(list[i]>k):
            k = list[i]
    list.remove(k)
    #print(list)        
    for i in range(len(list)):
        if(list[0]<=list[i]):
            t = list[i]
    print(f"the second highest no. is {t}")







secondhighest()

#Replace Negative Numbers with Zero

def replce():
    list = [4, -3, 7, -1, 0, 5]
    for i in range(len(list)):
        if(list[i]<0):
            list[i] = 0
    print(list)


replce()


print(set([1,2,2,3]))


#Reverse the List

#[1, 2, 3, 4, 5]

def reversing():
    lis = [1, 2, 3, 4, 5]
    M1 = int(len(lis))
    print(M1)
    M2 = M1-1
    print(M2)
    lis1 = []
    for i in range(M1):
        lis1.append(lis[M2-i])


        
            

    print(lis1)


reversing()


#Concatenate two lists index-wise####

def _init_():
    l1 = ["Hello", "Good"]
    l2 = ["World", "Morning"]
    l3 = [l1[0],l2[0]]
    l4 = [l1[1],l2[1]]
    ele1 = ''.join(l3)
    ele2 = ''.join(l4)
    l5 = [ele1,ele2]
    print(l5)

_init_()


#############Turn every item of a list into its square

def square():
    li = [1, 2, 3, 4, 5]
    for i in range(len(li)):
        li[i] = li[i]*li[i]

    print(li)    


square()

#####################

for i in range(1, 6):
    if i == 3:
        break
    print(i)

#x = 10
#x%=3

#print(x)


#print(10//3)


#Print(x)

##Strings Problems

Input= "hello"

print(Input[0])

def string_reverse():
    input = "hello"
    input_list = list()
    lent = len(input)
    m1 = lent -1
    reverse_list = []
    for i in range(lent):
        reverse_list[i] = input_list[m1-i]


    revesr_string = ''.join(reverse_list)
    print(revesr_string)    
        


        #string1[i] = input[m1 -i]

    



string_reverse()






    















       












