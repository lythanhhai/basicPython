'''import datetime as dt
t1 = dt.datetime.strptime('12:00:00', '%H:%M:%S')
t2 = dt.datetime.strptime('02:00:00', '%H:%M:%S')
time_zero = dt.datetime.strptime('00:00:00', '%H:%M:%S')
print((t1 - time_zero + t2).time())'''

h, m, s, x = map(int, input().split())
s += x
while s >= 60:
    m = m + 1
    s -= 60
while m >= 60:
    h = h + 1
    m -= 60
while h >= 12:
    h -= 12

print(h, end=" ")
print(m, end=" ")
print(s)
