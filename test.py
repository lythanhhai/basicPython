'''n = int(input())
count = 0
for i in range(n, n ** 2 + 1):
        count = count + 1
print(count)'''

from re import M
# định dạng giờ
'''
n = int(input())
print(n ** 2 - n + 1)

h = input()
m = input()
s = input()
print(h + ':' + m + ':' + s)
'''

# Số tự mãn

'''n = int(input())
m = str(n)
sum = 0
for i in m:
    sum += (int(i)**len(m))

if sum == int(m):
    print("YES")
else:
    print("NO")
'''


'''
n = int(input())
bin8 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(8)] ) )
print(bin8(n))
'''

# thừa số nguyên tố


'''def prime(m):
    if m < 2:
        return False
    for i in range(2, m):
        if m % i == 0:
            return False
    return True

n = int(input())
for i in range(2, n + 1):
    if prime(i) == True and n % i == 0:
        print(str(i), end=" ") '''


# biến đổi chuỗi
'''
sequence = input()
res = ''
for i in sequence:
    if ord(i) >= 97 and ord(i) <= 122:
        res += chr(ord(i) - 32)
    elif ord(i) >= 65 and ord(i) <= 90:
        res += chr(ord(i) + 32)
    else:
        res += i


print(res)
'''

# số nhị phân
'''
n = int(input())
m = 0
if n == 0:
    m = 1
k = []

while (n>0):
    a = int(float(n%2))
    k.append(a)
    n = (n-a)/2

res = ""

k.reverse()

for i in k:
    res += str(i)

if m == 1:
   res = 0

print(res)
'''

# giờ kết thúc làm bài
import datetime
import datetime as dt
h = int(input())
m = int(input())
s = int(input())
a = int(input())
h1 = ''
m1 = ''
s1 = ''
if len(str(h)) < 2:
    h1 += '0' + str(h) 
else:
    h1 += str(h) 
if len(str(m)) < 2:
    m1 += '0' + str(m) 
else:
    m1 += str(m) 
if len(str(s)) < 2:
    s1 += '0' + str(s) 
else:
    s1 += str(s) 
t = h1 + ':' + m1 + ':' + s1
t1 = str(datetime.timedelta(seconds=a)).split(':')
t1 = t1[0] + ':' + t1[1] + ':' + t1[2]

t2 = dt.datetime.strptime(t, '%H:%M:%S')
t3 = dt.datetime.strptime(t1, '%H:%M:%S')
time_zero = dt.datetime.strptime('00:00:00', '%H:%M:%S')
#print((t2 - time_zero + t3).time())

res = str((t2 - time_zero + t3).time()).split(":")
for i in res:
    if i[0] == '0':
        print(i[1], end=" ")
    else:
        print(i, end=" ")

'''
if a % 60 == 0:
    if s + a > 60:
        if m + a / 60 > 60:
            if h + a / 3600 > 60:
        else:
            print(str(h) + ' ' + str(m + a/60) + ' ' + str(s))
    else:
        print(str(h) + ' ' + str(m) + ' ' + str(s+a))
elif a % 3600 == 0:
    if a / 3600 + h > 12:
        print(str(a / 3600 + h - 12) + ' ' + str(m) + ' ' + str(s))
    else:
        print(str(h+a/3600) + ' ' + str(m) + ' ' + str(s))
else:
'''
