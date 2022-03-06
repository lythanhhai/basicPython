#2
# N = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# for i in arr:
#     print(i, end=" ")
#print(arr)

#4
# n = int(input())
# dict = {}
# for i in range(1, n + 1):
#     key, value = map(str, input().split())
#     if key in dict.keys():
#         dict[key] = dict[key] + " " + value
#     else:
#         dict[key] = value

# count = 0

# for i in dict:
#     if len(set(dict[i].split())) >= 2:
#         count += 1

# print(count)


#7
# def fibonacci(n):
#     f0 = 0
#     f1 = 1
#     fn = 1
 
#     if (n == 0 or n == 1):
#         return n
#     else:
#         for i in range(2, n):
#             f0 = f1
#             f1 = fn
#             fn = f0 + f1
#         return fn

# arrFibo = []
# n = int(input())
# for i in range(0, n):
#     arrFibo.append(fibonacci(i))

# res = lambda a: a ** 3
# print(list(map(res, arrFibo)))


#5
# N = int(input())
# List = list(map(int, input().split()))
# def maxLen(arr):
     
#     hash_map = {}

#     max_len = -1

#     curr_sum = 0

#     for i in range(len(arr)):

#         curr_sum += arr[i]
 
#         if arr[i] is 0 and max_len is 0:
#             max_len = 1
 
#         if curr_sum is 0:
#             max_len = i + 1
 
#         if curr_sum in hash_map:
#             max_len = max(max_len, i - hash_map[curr_sum] )
#         else:
#             hash_map[curr_sum] = i
 
#     return max_len

# print(maxLen(List))

# 3
# def binary_search(arr, low, high, x):
#     if(x < arr[0]):
#         return -1
#     if high >= low:

#         mid = (high + low) // 2

#         if arr[mid] == x:
#             return arr[mid]

#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)

#         else:
#             return binary_search(arr, mid + 1, high, x)

#     else:
#         return arr[(high + low) // 2]

# N = int(input())
# V = list(map(int, input().split()))
# M = int(input())
# List = []

# for i in range(M):
#     a = int(input())
#     List.append(binary_search(V, 0, len(V) - 1, a))

# for i in range(len(List)):
#     print(List[i])



#1111
m, n = map(int, input().split())

arr = []
for i in range(0, m):
    row = input()
    arr.append(row)

maze = [[0]*n for _ in range(m)]
if arr[-1][-1] == "#":
    count = -1
    print(count)
else:
    for i in range(0, m):
        for j in range(0, n):
            if arr[i][j] == ".": 
                maze[i][j] = 0
            else:
                maze[i][j] = 1

    solution = [[0]*n for _ in range(m)]
    count = 0

    def solvemaze(r, c):

        if (r==m-1) and (c==n-1):
            solution[r][c] = 1
            return True

        if r>=0 and c>=0 and r<m and c<n and solution[r][c] == 0 and maze[r][c] == 0:
            solution[r][c] = 1
            # xuống
            if solvemaze(r+1, c):
                return True
            # phải
            if solvemaze(r, c+1):
                return True
            # lên
            if solvemaze(r-1, c):
                return True
            # trái
            if solvemaze(r, c-1):
                return True
            #backtracking
            solution[r][c] = 0
            return False
        return 0

    if(solvemaze(0, 0)):
        for i in solution:
            for j in i:
                if j == 1:
                    count += 1
    else:
        count = -1

    if count == -1:
        print(count)
    else:
        print(count - 1)



# def min_solution(maze, x = 0, y = 0, path = None):
#     def try_next(x, y):
#         return [(a, b) for a, b in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)] if 0 <= a < n and 0 <= b < m]

#     n = len(maze)
#     m = len(maze[0])
    
#     if path is None:
#         path = [(x, y)]

#     if x == n - 1 and y == m - 1:
#         return path
    
#     maze[x][y] = 1
    
#     shortest_path = None            
#     for a, b in try_next(x, y):
#         if not maze[a][b]:
#             last_path = min_solution(maze, a, b, path + [(a, b)])
            
#             if not shortest_path:
#                 shortest_path = last_path
#             elif last_path and len(last_path) < len(shortest_path):
#                 shortest_path = last_path
     
    
#     maze[x][y] = 0 
    
#     return shortest_path

# t = min_solution(maze)
# if t:
#     print(len(t) - 1)
# else:
#     count = -1
#     print(count)
