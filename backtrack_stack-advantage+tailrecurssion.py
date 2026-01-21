'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")

#stacks and queue

#stack 
#push and  pop 

#queue

#enque and deque


# infix and postfix

#Postfix expression (also called Reverse Polish Notation - RPN) 
#is a way of writing 
#expressions without parentheses where the operator comes after 
#the operands


#linked list
print('linked list')


#N quene problem in backtracking
N = 4
board = [[0]*N for _ in range(N)]

print(board)

def issafe(board,row,col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i,j = row -1,col -1 
    while i >= 0 and j >= 0:
        if board[i][j] == 1 :
            return False
        i -= 1 
        j -= 1 
    i,j = row - 1,col + 1 
    while i >= 0 and j < N :
        if board[i][j] == 1:
            return False
            
        i -= 1 
        j += 1 
    return True
    
    
def solve_N_quen(board,row):
    if row == N:
        return True
    for col in range(N):
        if issafe(board,row,col):
            board[row][col] = 1 
            if solve_N_quen(board,row + 1):
                return True
            board[row][col] = 0 
    return False
    
    
    
#factorial recurssion  devide and conquer

def factorial(N):
    if N <= 1:
        return 1 
    else:
        return N*factorial(N-1)
        
#factorial using iteration 

def factorial_iter(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
    
        
#Call Stack Explanation: When a recursive function calls itself, 
#the current state is saved on a stack called the call stack. 
#Each function call adds a new frame to the stack with parameters and local variables.
#When a base case is reached, the function returns, popping the stack frame, 
#unwinding the recursion.        

    
 #Tail Recursion is a special case of recursion 
 #where the recursive call is the last operation in the function.   

def factorial_tail(n, acc=1):
    if n == 0 or n == 1:
        return acc
    else:
        return factorial_tail(n - 1, acc * n)
 
            
        
            
    
    
    
    
    
    
    
    
    
    
    





