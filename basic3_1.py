
#3
# import math
# N = int(input())
# V = list(map(int, input().split()))
# M = int(input())
# List = []
# for i in range(0, M):
#     a = int(input())
#     List.append(a)
# for i in list:
#     for j in range(0, len(V)):
#         if i >= V[-1]:
#             print(V[-1])
#             break
#         elif i < V[j] and j > 0:
#             print(V[j - 1])
#             break
#         elif i < V[j] and j == 0:
#             print("-1")
#             break
#         else:
#             continue


# count = 1
# max = -1
# sumCurrent = 0
# for i in range(0, len(List) - 1):
#     sumCurrent = List[i]
#     count = 1
#     for j in range(i + 1, len(List)):
#         sumCurrent = sumCurrent + List[j]
#         count += 1
#         if sumCurrent == 0:
#             max = count
#         else:
#             continue

# print(max)

1
m, n = map(int, input().split())

arr = []
for i in range(0, m):
    row = input()
    arr.append(row)

count = 0
indexRow = 0
indexCol = 0
for i in range(0, m):
    if indexRow == m - 1 and indexCol == n - 1:
        break
    if count == -5:
        break
    if "." not in arr[i]:
        count = -1
        break
    for j in range(0, n):
        if indexRow == m - 1 and indexCol == n - 1:
            break
        if arr[i][j] == "#":
            continue
        if i != m - 1 and j != n -1:
            if arr[i+1][j] == ".":
                indexRow = i + 1
                indexCol = j
                count += 1
                break
            elif arr[i][j+1] == ".":
                indexRow = i
                indexCol = j + 1
                count += 1
            elif arr[i][j-1] == ".":
                indexRơw = i
                indexCol = j - 1
                count -= 1
            elif arr[i-1][j] == ".":
                indexRow = i - 1
                indexCol = j
                count -= 1
                break
            else:
                count = -5
                break
        elif i == m - 1:
            if arr[i][j+1] == ".":
                indexRow = i
                indexCol = j + 1
                count += 1
            elif arr[i][j-1] == ".":
                indexRơw = i
                indexCol = j - 1
                count -= 1
            elif arr[i-1][j] == ".":
                indexRow = i - 1
                indexCol = j
                count -= 1
                break
            else:
                count = -5
                break
        elif j == n - 1:
            if arr[i+1][j] == ".":
                indexRow = i + 1
                indexCol = j
                count += 1
                break
            elif arr[i][j-1] == ".":
                indexRơw = i
                indexCol = j - 1
                count -= 1
            elif arr[i-1][j] == ".":
                indexRow = i - 1
                indexCol = j
                count -= 1
                break
            else:
                count = -5
                break
        else:
            break

print(count)
