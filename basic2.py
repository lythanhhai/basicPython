#1
# n = int(input())
# count = 0
# for i in range(1, n**2 + 1):
#     if i % 2 == 0 or i % 3 == 0:
#         count = count + 1
# print(count)

#2
# n, a, b = map(int, input().split())
# count = 0
# for i in range(1, n + 1):
#     if i % a == 0 or i % b == 0:
#         count = count + 1
# print(count)

#2 C2
# def uscln(a, b):
#     if (b == 0):
#         return a
#     return uscln(b, a % b)

# def bscnn(a, b):
#     return int((a * b) / uscln(a, b))

# n, a, b = map(int, input().split())
# count = 0
# count = int(n/a) + int(n/b)
# common = int(n / (bscnn(a, b)))
# if a == b:
#     print(int(count/2))
# else: 
#     print(int(count) - common)

#print(common)
#3

# def solve(n, k):
#     x = int(k/(n-1))
#     r = k%(n-1)
#     if r == 0:
#         return x * n - 1
#     else:
#         return n * x + r

# q = int(input())
# count = 0
# arr = []
# for i in range(1, q + 1):
#      a, b = map(int, input().split())
#      arr.append([a, b])

# for i in arr:
#     print(int(solve(i[0], i[1])))
    

#4
# string = input()
# indexCurrent = 0

# res = ""
# while indexCurrent < len(string) - 3:
#     if int(string[indexCurrent] + string[indexCurrent+1]) >= 65 and int(string[indexCurrent] + string[indexCurrent+1]) <= 90 or int(string[indexCurrent] + string[indexCurrent+1]) >= 97 and int(string[indexCurrent] + string[indexCurrent+1]) <= 99:
#         res = res + string[indexCurrent] + string[indexCurrent + 1] + " "
#         indexCurrent = indexCurrent + 2
#     else: 
#         res = res + string[indexCurrent] + string[indexCurrent + 1] + string[indexCurrent + 2] + " "
#         indexCurrent = indexCurrent + 3


# if len(string) - 3 == indexCurrent:
#     res += string[-3] + string[-2] + string[-1]
# else:
#     res += string[-2] + string[-1]

# resFinal = ""
# for i in res.split(" "):
#     resFinal += chr(int(i))

# print(resFinal)

#5 


#6
# n, k = map(int, input().split())
# t = input()
# arr = list(int(x) for x in t.split(' '))
# arr.sort()
# sum = 0
# for i in range(0, k):
#     sum += arr[i]
# print(sum)

#7

n = int(input())
arr = list(input().split(' '))
arr.sort()
arr1 = list(input().split(' '))
arr1.sort(reverse=True)
print(arr)
print(arr1)
cost = 0
for i in range(0, len(arr)):
    cost += int(arr[i]) * int(arr1[i])
print(cost)

#8
# n = int(input())
# arr = list(int(x) for x in input().split(' '))
# res = list(dict.fromkeys(arr))
# res.sort()
# print(len(res))
# for i in res:
#     print(i)


#9

# n, m = map(int, input().split())
# t = input()
# arr = list(int(x) for x in t.split(' '))
# t1 = input()
# arr1 = list(int(x) for x in t1.split(' '))
# res = list(dict.fromkeys(arr))

# print(len(set(res) & set(arr1)))


# 10

# n = int(input())
# arr = []
# for i in range(1, n + 1):
#      a, b = map(str, input().split())
#      arr.append([a, b])

# res = dict.fromkeys(arr)
# print(res)
# temp = []
# res = []
# sum = 0
# for i in range(0, len(arr) - 1):
#     sum = int(arr[i][1])
#     if arr[i][0] not in temp: 
#         for j in range(i+1, len(arr)):
#             if arr[i][0] == arr[j][0]:
#                 sum += int(arr[j][1])
#         res.append(sum)
#         sum = 0
#         temp.append(arr[i][0])
#     else:
#         continue

# if(arr[-1][0] not in temp):
#     res.append(int(arr[-1][1]))
#     temp.append(arr[-1][0])

# # tìm giá trị lớn nhất
# max = res[0]
# index = 0
# for i in range(1, len(res)):
#     if res[i] > max:
#         max = res[i]
#         index = i

# print(temp[index] + " " + str(max))