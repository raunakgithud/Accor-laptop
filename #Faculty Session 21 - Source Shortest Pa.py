#Faculty Session 21 - Source Shortest Path
print("graph theory")
#Dijkstra's algorithm
def Dijkstra(graph,s):
    visited = set()
    
    dist = {s: 0}
    while visited is None:
        for edge in graph[s]:
            weight,u,v = graph[s].pop()
            visited.add(u)
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
    return dist             
            

a= [1,4,6,8]
s = a.pop()
print(s)

def fn(arr, n, k):
    a = [[0] * k for _ in range(n - k + 1)]

    l = len(a)
    w = len(a[0])

    for i in range(l):
        for j in range(w):
            a[i][j] = arr[i + j]

    for i in range(l):
        print(max(a[i]), end=" ")

#implimentation of Dijkstra using priority queue
def priority(u, v, weight_uv, dist, heap):
    if dist[u] + weight_uv < dist[v]:
        dist[v] = dist[u] + weight_uv
        heap.decrease_key(v, dist[v])


