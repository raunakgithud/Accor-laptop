#practice_DP

N = 4
jump = [1,2,3]
a = []
c = 0
for i in range(len(jump)):
    remaining = N - jump[i]
    c += 1
    a.append(remaining)
print(a)
#def staircase(N,jump):
#    if N == 0:
#        q = 0
#    else:
#        q = -100000000
#        for i in range(len(jump)-1):
#            q = max(q,1 + staircase(N - jump[i],jump))
#    return q
#print(staircase(N,jump))   


#subproblem

#prefix   n
#suffix   n
#substring   n**2


#for i in range(len(jump)-1):
#    remaining = N - jump[i]
#    count += 1
#    while remaining > 0:
#        remaining -= jump[i]
#        count += 1
#print(count)
# 
#def stair(N,j):
#    c = []
#    for i in j:
#        remain = N-i
#        count = 1
#        while remain > 0:
#            stair(N-i,j)
#            count += 1
#        c.append(count)
#    return c    



    
#print(stair(4,[1,2,3]))    


#bank
#n  > n//2, n//3,  n//4
#exchange
#n gold to n rupee
# 
def Masai_coin(n):
    case = [0]*2
    #case[0],bank
    if n >= 1:
        case[0] = (n//2 +n//3 +n//4)
    else:#case[1] , exchange
        case[1] = n
    return max(case)    

print(Masai_coin(6))
print(Masai_coin(12))



    
