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

N = 4

def printSolution( sol ):
	
	for i in sol:
		for j in i:
			print(str(j) + " ", end ="")
		print("")

def isSafe( maze, x, y ):
	
	if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
		return True
	
	return False

def solveMaze( maze, m, n ):
	
	sol = [ [ 0 for j in range(m) ] for i in range(n) ]
	
	if solveMazeUtil(maze, 0, 0, sol) == False:
		return False
	
	printSolution(sol)
	return True
	
def solveMazeUtil(maze, x, y, sol):

	if x == N - 1 and y == N - 1 and maze[x][y]== 1:
		sol[x][y] = 1
		return True
		
	if isSafe(maze, x, y) == True:

		if sol[x][y] == 1:
			return False
		
		sol[x][y] = 1
		
		if solveMazeUtil(maze, x + 1, y, sol) == True:
			return True

		if solveMazeUtil(maze, x, y + 1, sol) == True:
			return True

		if solveMazeUtil(maze, x - 1, y, sol) == True:
			return True
			
		if solveMazeUtil(maze, x, y - 1, sol) == True:
			return True
		
		sol[x][y] = 0
		return False

if __name__ == "__main__":

	maze = [ [1, 0, 0, 0],
			[1, 1, 0, 1],
			[0, 1, 0, 0],
			[1, 1, 1, 1] ]
			
	solveMaze(maze, 4, 4)

