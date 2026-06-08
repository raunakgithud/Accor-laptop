#Dynamic_programming
#to reduce the time complexity of fibonaccies from exponential
#to polinomial
#1. cut rod p = [prices]  n = size of the rod

def cutrod(p,n):
    if n == 0:
        return 0
    q = 0
    for i in range(n):
        q = max(q,p[i] + cutrod(p,n-i+1))
    return q  

#T.C for the above solution is exponential O(2**n) 
#with help of memoization 

def memoized_cutrod(p,n,r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1,n+1):
            q = max(q,p[i]+memoized_cutrod(p,n-i,r))
    r[n] = q
    return q

print([0]*3)
print([[0]*i] for i in range(3))

#SRTBOT problem solutions 
#steps below:

#subproblem definition
#relation
#topology order(recurse to end)
#base case[terminating condition]
#original problem
#time complexity

#string of n lenght can form how many numbers of subsequence
#longest common subsequence among two strings |A|  |B|

def LCS(A,B):
    m = len(A)
    n = len(B)
    l = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if A[i] == B[j]:
                l[i][j] = 1 + l[i+1][j+1]
            else:
                l[i][j] = max(l[i+1][j],l[i][j+1])
    return l[0][0]




   

def cut(p,n):
    
    dp = [0]*(n+1)
    if n == 0:
        return 0
    if n == 1:
        return 2
    
    for i in range(1,n+1):
        max_profit = 0
        for j in range(len(p)):
         if(i > j):
          max_profit = max(max_profit,p[j] + dp[i-j-1])
          dp[i] = max_profit
    return dp[n] 
p = [2, 5, 7, 8]
print(cut(p,5))   
    
def coin(n):
    
    if n%2 == 0 and n%3==0 and n%4 == 0:
        return (n//2 + n//3 + n//4)
    return n

print(coin(12))



