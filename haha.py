# def MaximumPath(grid):
 
#     N = len(grid)
#     M = len(grid[0])
 
#     sum = [[0 for i in range(M + 1)]
#               for i in range(N + 1)]
 
#     for i in range(1, N + 1):
#         for j in range(1, M + 1):
 
#             sum[i][j] = (max(sum[i - 1][j],
#                              sum[i][j - 1]) +
#                         grid[i - 1][j - 1])
 
#     # return sum[N][M]
#     return sum
 

# n = int(input())
# grid = []
# for i in range(n):
#     grid.append(list(map(int, input().split())))
# a = 2
# #print(MaximumPath(grid), a, sep=" ")
# print(MaximumPath(grid))
 


allPaths = []
def findPaths(maze,m,n):
    path = [0 for d in range(m+n-1)]
    findPathsUtil(maze,m,n,0,0,path,0)
     
def findPathsUtil(maze,m,n,i,j,path,index):
    global allPaths

    if i == m-1:
        for k in range(j,n):
            path[index+k-j] = maze[i][k]
        allPaths.append(sum(path))
        return
    if j == n-1:
        for k in range(i,m):
            path[index+k-i] = maze[k][j]
        allPaths.append(sum(path))
        return

    path[index] = maze[i][j]
     
    findPathsUtil(maze, m, n, i+1, j, path, index+1)
     
    findPathsUtil(maze, m, n, i, j+1, path, index+1)

n = int(input())
maze = []
for i in range(n):
    maze.append(list(map(int, input().split())))

findPaths(maze, n, n)
count = 0
for i in allPaths:
    if i == max(allPaths):
        count += 1
        
print(max(allPaths), count, sep=" ")