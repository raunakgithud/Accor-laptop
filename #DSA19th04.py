#DSA

print('DSA')
#Two pointer
def two_sum(arr,T):
    arr.sort()
    low = 0
    high = len(arr)-1
    while low < high :
        if arr[low] + arr[high] == T:
            return True
        if arr[low] + arr[high] > T:
            high -= 1
        if arr[low] + arr[high] < T:
            low += 1    

#palamdrome
def is_palindrome(s):
    low , high = 0,len(s) -1            
    while low < high :
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True


    
