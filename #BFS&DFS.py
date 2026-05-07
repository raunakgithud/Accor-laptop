#BFS&DFS
print('BfS_DfS')

#vertex = node

#T.c. is O(E+V)
#connected graph G means between every two vertices there should be
#one path exists between them 
#if the graph is not connected then BFS will not return the total
#N number of vertices (in visited data structure)

#what is the shortest path btn two random nodes of an weighted 
#graph


#How BFS works:
#
#Choose any vertex as the source node.
#Mark the source vertex as visited and enqueue it.
#While the queue is not empty:
#Dequeue the front vertex from the queue.
#Process (e.g., print) this vertex.
#For each unvisited adjacent vertex of the dequeued vertex:
#Mark it as visited.
#Enqueue it.

from collections import deque

def bfs(graph,start):
    visited = set()
    queue = []
    queue.append(start)
    visited.add(start)
    while queue :
        vertex = queue.pop()
        print(vertex,end=" ")
        for nei in graph[vertex]:
            if nei not in visited :
                visited.add(nei)
                queue.append(nei)


graph = {
    0: [1, 3],
    1: [0, 2, 5, 6],
    2: [1, 3, 5],
    3: [0, 2, 4],
    4: [3, 6],
    5: [1, 2],
    6: [1, 4]
}

print(bfs(graph,0))#0 3 4 6 2 5 1 None
print(bfs(graph,1))#1 6 4 3 5 2 0 None
print(bfs(graph,2))#2 5 3 4 6 0 1 None
print(bfs(graph,3))#3 4 6 1 5 2 0 None
print(bfs(graph,4))#4 6 1 5 2 0 3 None
#hence graph is a connected graph 
#bfs can also be used to find the shortest path between two 
#two nodes

def shortest_path_iter(graph,s,t):
    visited = set()
    queue = []
    queue.append(s)
    distence = {s:0}
    while queue :
        vertex = queue.pop()
        if vertex == t :
            return distence[vertex]
        for nei in graph[vertex] :
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
                distence[nei] = distence[vertex]+1
    return -1   

print(shortest_path_iter(graph,0,6))#3
print(shortest_path_iter(graph,0,1))#1
print(shortest_path_iter(graph,0,3))#1  
print(shortest_path_iter(graph,1,6))#1
print(shortest_path_iter(graph,3,6))#2   

print('==========================================')


print('DFS')

#Start at any vertex.
#Mark it as visited and push it on a stack (or enter recursion).
#Go to one unvisited neighbor, mark it visited, push it, and continue.
#If you reach a vertex with no unvisited neighbors, pop vertices or return from recursion to backtrack.
#Repeat until all vertices reachable from the start node are visited.

#Iterative

def dfs_iterative(graph,start):
    stack = [start]
    visited = set()
    visited.add(start)
    while stack:
        vertex = stack.pop()
        print(vertex,end=" ")
        for nei in graph[vertex]:
            if nei not in visited :
                visited.add(nei)
                stack.append(nei)

print(dfs_iterative(graph,4))#4 6 1 5 2 0 3 None
print(dfs_iterative(graph,0))#0 3 4 6 2 5 1 None
print(dfs_iterative(graph,6))#6 4 3 2 5 0 1 None

print("------------------------------------------------")
#DFS recursive

def DFS_recursive(graph,vertex,visited = None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex,end=" ")
    for nei in graph[vertex] :
        if nei not in visited :
            DFS_recursive(graph,nei,visited)


print(DFS_recursive(graph,0))#0 1 2 3 4 6 5 None
print(DFS_recursive(graph,6))#6 1 0 3 2 5 4 None
print(DFS_recursive(graph,4))#4 3 0 1 2 5 6 None            
print(DFS_recursive(graph,1))#1 0 3 2 5 4 6 None





