#Graph in detail 
#https://students-old.masaischool.com/lectures?tab=all



graph = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

print(graph)


#Graph implementations 

vertexData = [ 'A', 'B', 'C', 'D']

adjacency_matrix = [
    [0, 1, 1, 1],  # Edges for A
    [1, 0, 1, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D
]

def print_adjmatrix(graph):
    print('\n adj matrix listed below')
    for row in graph:
        print(row)

print(print_adjmatrix(adjacency_matrix))    

#DSA Graphs Traversal
#Faculty Session 25 - Amortized Analysis

#Depth First Search Traversal

class graph:
    def __init__(self,size):
        self.adj_matrix = [[0]* size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
        


#Faculty Session 23 - Union - Find Data Structure
#g = (v,e)
#n = len(g(v))
#m = len(g(e))
#e = (v[i],v[j])

#initialy 
#x = [{'v1'},{'v2'},{'v3'},{'v4'},{'v5'}] # v n number of vetexes
#
#e = sorted('e1','e2','e3','em') # for a mst e weight should be minimum
#for i in range(m):
#    for j in range(m):
#        e[i] = (x[i],x[j])



p = {} # should ne directory not a list

def make_set(v):
    p[v] = v

def find(a):
    if p[a] == a :
        return a
    return p[a]

def union(a,b):
    a_lead = p[a]
    b_lead = p[b]
    if a_lead != b_lead :
        p[a_lead] = b_lead

make_set('A')
make_set('B')
union('A','B')
print(p)

make_set('C')
union('A','C')
print(p)

make_set('E')
make_set('D')
union('D','E')
print(p)
union(find('E'),find('D'))
print(p)

#print(find('h'))

# union and find is upperbounded by log n , tc <= log n 


#Union-find DS working start from the parent node 
#Two main optimization method is 

#Union by rank 
#path compression


class Uniofind:
    def __init__(self,n):
        self.parent = list(range(n)) # to create a graph
        self.rank = [0]*n #list of edges with weight 
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        x_lead = self.find(x)
        y_lead = self.find(y)
        if x_lead != y_lead :
            if self.rank[x_lead] < self.rank[y_lead] :
                self.parent[x_lead] = y_lead
            if self.rank[x_lead] > self.rank[y_lead] :
                self.parent[y_lead] = x_lead
            else:
                self.parent[y_lead] = x_lead
                self.rank[x_lead] += 1


                
                       

        



          
     












        
