#Two_pointers
# merge sort
# cycle detection 
#Two  

#Given a sorted array and a target value, find out if there exists any two numbers whose 
#summation equals the target value.

def twosumsorted(arr,target):
    left = 0
    right = len(arr) - 1
    
    
        
        
    while right > left:
        sum = arr[left] + arr[right]
        if sum == target:
            return left,right

        if target > sum:
            left += 1
        if target < sum:
            right -= 1
    


print(twosumsorted([1, 3, 4, 5, 7, 10, 11],9))

#The sliding window technique is used to find the maximum sum 
#of any 
#contiguous subarray of a fixed size k efficiently.

#Calculate sum of every subarray of size k

def maxsumsubarray(arr,k):
    windowsum = 0
    for i in range(k):
        windowsum += arr[i]
    maxsum = windowsum
    for i in range(k,len(arr)):
        windowsum += arr[i] - arr[i-k] 
        maxsum = max(maxsum,windowsum)
    return maxsum


print(maxsumsubarray([2, 1, 5, 1, 3, 2],3))


#Given an array of positive integers and a target sum, 
#find the minimum length of a contiguous subarray such 
#that the sum of the subarray is at least the target. 
#If no such subarray exists, return 0.


#This problem can be solved using a variable size sliding window 
#technique.

def minSubarrLen(arr,target):
    left = 0
    sum = 0
    minLen = 100000

    for right in range(len(arr)-1):
        sum += arr[right]
        while sum >= target:
            minLen = min(minLen,(right-left+1))
            sum -= arr[left]
            left += 1 
    return minLen

print(minSubarrLen([2,3,1,2,4,3],7))

#container with most water

#Given an array representing the heights of vertical 
#lines drawn on x-axis
#find two lines such that they with the x-axis form 
#a container that holds the maximum water.

def maxArea(arr):
    left = 0
    right = len(arr)-1
    #area = min(arr[left],arr[right]) * (right-left)
    areaMax = 0
    while left < right:
        area = min(arr[left],arr[right]) * (right-left)
        areaMax = max(areaMax,area)
        if (arr[left]<arr[right]):
            left += 1
        else:
            right -= 1
    return areaMax

print(maxArea([1,8,6,2,5,4,8,3,7]))     


nums = [0 ,1, 0 ,12, 3]

def moveZero(arr):
    moved = []
    start = 0
    while start < len(arr):
        if arr[start] != 0:
            moved.append(arr[start])
        start += 1 
    while len(moved) != len(arr):
        moved.append(0)
    for i in range(len(moved)):
        print(moved[i], end= " ")
print(moveZero(nums))            



#5 9
#3 0 6 2 7


def pairNo(arr,target):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr),1):
            if arr[i] + arr[j] == target:
                count += 1
    return count            
 
print(pairNo([3, 0, 6, 2, 7],9))


def maxcontigious(arr):
    left = 0
    right = len(arr)
    sum = 0
    while left < right:
        currentsum =sum+arr[left]
        if currentsum >= sum:
            sum = currentsum
            maxsum = sum
        else:
            maxsum = currentsum - arr[left]   
            sum = 0 
        left += 1
    return max(maxsum,currentsum)

case1 = [1, 2, 0, 4, 5]
case2 = [3, -4, 1, 2, -1]
print(maxcontigious(case1))    
print(maxcontigious(case2))     

case4 = [[1,3],[5,6],[2,4]]


