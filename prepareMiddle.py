# 1. check array sum of pair

# def printPairs(arr, sum):
     
#     hashmap = {}
     
#     for i in range(0, len(arr)):
#         temp = sum - arr[i]
#         if (temp in hashmap):
#             return True
#         hashmap[arr[i]] = i
    
#     return False

# N, K = map(int, input().split())
# A = list(map(int, input().strip().split()))

# if printPairs(A, K):
#     print("Yes")
# else:
#     print("No")

# 2. convert decimal to hexadecimal

# n = int(input())

# hexadecimal = hex(n).split("x")[1]
# hexadecimal = (8 - len(hexadecimal)) * '0' + hexadecimal

# count = 1
# res = ""
# print(hexadecimal)

# for index in range(0, len(hexadecimal)):
#     if ord(hexadecimal[index]) >= 97 and ord(hexadecimal[index]) <= 122:
#         if count % 4 == 0:
#             res += chr(ord(hexadecimal[index]) - 32) + " "
#         else:
#             res += chr(ord(hexadecimal[index]) - 32)
#     else:
#         if count % 4 == 0:
#             res += hexadecimal[index] + " "
#         else:
#             res += hexadecimal[index]
    
#     count += 1

# print(res)

# 3. Nami plant orange on the boat, namely sunny

import time
start_time = time.time()

# N, M = map(int, input().split())
# Start = []
# for i in range(N):
#     L = list(map(int, input().strip().split()))
#     Start.append(L)

def find_neighbours(arr):

    neighbors = []

    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):

            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                # corners
                new_neighbors = []
                if i != 0:
                    new_neighbors.append(arr[i - 1][j])  # top neighbor
                if j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i][j + 1])  # right neighbor
                if i != len(arr) - 1:
                    new_neighbors.append(arr[i + 1][j])  # bottom neighbor
                if j != 0:
                    new_neighbors.append(arr[i][j - 1])  # left neighbor

            else:
                # add neighbors
                new_neighbors = [
                    arr[i - 1][j],  # top neighbor
                    arr[i][j + 1],  # right neighbor
                    arr[i + 1][j],  # bottom neighbor
                    arr[i][j - 1]   # left neighbor
                ]

            neighbors.append({
                "value": value,
                "neighbors": new_neighbors})

    return neighbors
    
print(find_neighbours([[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]))
print("--- %s seconds ---" % (time.time() - start_time))


# 4.

# 5. Triangle position

# L = list(map(int, input().strip().split()))
# def checkTriangle(x1, y1, x2, y2, x3, y3):

#     a = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
         
#     if a == 0:
#         print('No')
#     else:
#         print('Yes')

# checkTriangle(L[0], L[1], L[2], L[3], L[4], L[5])

# 6. Array

# def singleNumber(array):
#         ones = 0
#         twos = 0
#         for ele in array:
#             ones = (ones ^ ele) & (~twos)
#             twos = (twos ^ ele) & (~ones)
#         return ones

# T = int(input())
# arrayN = []
# arrayL = []
# for i in range(T):
#     N = int(input())
#     arrayN.append(N)
#     L = list(map(int, input().strip().split()))
#     arrayL.append(L)

# for item in arrayL:
#     print(singleNumber(item))

# 7. regex(easy)
