allPaths = []

def findPaths(mat, path, i, j):
 
    if not mat or not len(mat):
        return
        
    (M, N) = (len(mat), len(mat[0]))

    if i == M - 1 and j == N - 1:
        #print(path + [mat[i][j]])
        allPaths.append(path + [mat[i][j]])
        return

    path.append(mat[i][j])

    if 0 <= i < M and 0 <= j + 1 < N:
        findPaths(mat, path, i, j + 1)

    if 0 <= i + 1 < M and 0 <= j < N:
        findPaths(mat, path, i + 1, j)

    path.pop()
 

path = []

n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

x = y = 0

findPaths(mat, path, x, y)

count = 0
for i in allPaths:
    if i == max(allPaths):
        count += 1
        
print(sum(max(allPaths)), count, sep=" ")