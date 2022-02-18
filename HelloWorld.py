from tkinter import N


'''M = "Tuấn"
N = 8
print("Tôi tên là " + M)'''


'''N = int(input())
count = 0
if N < 10000000:
    for i in range(1, int(N / 2 + 1)):
        if (N % i == 0):
            count = count + 1
    print(count + 1)
else:
    for i in range(1, int(N ** (1/2) + 1)):
        if (N % i == 0):
            count = count + 1
    print(count * 2 - 1)'''


'''n = int(input())
count = 0
for i in range(n, n ** 2 + 1):
        count = count + 1

print(n)'''

# bài cuối 
'''N = int(input())
arr = []

for i in range(0, N):
    arr.append([])
    for j in range(0, 2):
        x = int(input())
        arr[i].append(x)

arrRes = []
for i in range(0, N):
    sum = 0
    for j in range(0, 2):
        sum += arr[i][j]
    arrRes.append(sum)

for i in range(0, N):
    print(arrRes[i])'''

# import sys
# sys.setrecursionlimit(100000)
N = int(input())

arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append(a + b)

for i in arr:
    print(i)



    #print(arr[i])
'''print("Day so vua nhap la: ")
for i in range(0, N):
    for j in range(0, 2):
        print("%3d " % arr[i][j], end='')
    print()s'''