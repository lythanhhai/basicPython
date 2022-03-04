def move(P, i, m, n):
    if i == 0:
        if P[0] < m - 1:
            return P[0] + 1, P[1]
    if i == 1:
        if P[1] < n - 1:
            return P[0], P[1] + 1
    return None

n = int(input())
maze = []
for i in range(n):
    maze.append(list(input().split()))

start = (0, 0)
goal = (n-1, n-1)

pathBiggest = -1
count = 0

Open = [(start, 0, None)]
Closed = {start}
res = []
while Open:
    O_TT = Open.pop(0)
    O = O_TT[0]

    if O == goal:
        # if pathBiggest == -1:
        #     pathBiggest = O_TT[1]
        # elif pathBiggest > O_TT[-1]:
        #     pathBiggest = O_TT[-1]
        #res.append(O_TT[-1])
        break

    for i in range(2):
        child = move(O, i, n, n)
        if child and child not in Closed:
            Open.append((child, O_TT[1] + 1, O_TT))
            Closed.add(child)

print(len(res))
print(res)
print(pathBiggest)