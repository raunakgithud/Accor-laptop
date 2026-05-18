#primsAlgo_huffman

#https://students-old.masaischool.com/lectures/132774?tab=concepts
#Faculty Lecture 15 - Prims algo and huffman coding
#goal is T.C < O(log n)
#max_heap  time complexity O(nlog n)

#heap_sort algo
#how many partions can you have in a n vertex graph
#we need not to check the cycle in a graph to form a 
#minimum spanning tree

#Time complexity for the primes algorithm is O(|E||V|)

from heapq import heappush,heappop
def primalgo(graph):
    mst = []
    visited = set()
    min_heap = []
    start_vertex = 0
    visited.add(start_vertex)
    for edge in graph[start_vertex]:
        if edge not in visited:
            visited.add(edge)
            heappush(min_heap,edge)
    while min_heap:
        weight,u,v = heappop(min_heap)
        if v not in visited:
            visited.add(v)
            mst.append(u,v,weight)
            for next_edge in graph[v]:
                if next_edge not in visited:
                    heappush(min_heap,edge)
    return mst


#Huffman coding and implimentation 
#https://students-old.masaischool.com/lectures/133973?tab=concepts

#huffman is lossless data compression method 
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

#time complexity O(2^n) exponential

#Top down Dp of fib 

def dynamic_fib(n):
    memo = {}
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        memo[n] = 1
        return 1
    memo[n] = dynamic_fib(n-1) + dynamic_fib(n -2)
    return memo[n]

#Bottom up Dynamic programming

def dynamic_fibbottom(n):
    if n == 1 or n == 2:
        return 1 
    dp = [0]*(n+1)
    dp[1], dp[2] = 1,1
    for i in range(3,n+3):
        dp[n] = dp[n-1] + dp[n-2]
    return dp[n]
    



