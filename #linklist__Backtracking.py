#linklist__Backtracking

N = 4
board = [[0] * N for _ in range(N)]

print(board)

def is_safe(board,row,col):
    for i in range(row):
        if board[i][col] == 1:
            return False
        i,j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1







#Recursion can be elegant but may be inefficient.
#Repeated subproblems → think dynamic programming or memoization.

#Faculty Session 11 - Backtracking

 
