def move(P, i, m, n):
    if i == 0:
        if P[0] > 0:
            if maze[P[0] - 1][P[1]] == '.':
                return P[0] - 1, P[1]
    if i == 1:
        if P[0] < m - 1:
            if maze[P[0] + 1][P[1]] == '.':
                return P[0] + 1, P[1]
    if i == 2:
        if P[1] > 0:
            if maze[P[0]][P[1] - 1] == '.':
                return P[0], P[1] - 1
    if i == 3:
        if P[1] < n - 1:
            if maze[P[0]][P[1] + 1] == '.':
                return P[0], P[1] + 1
    return None

m, n = map(int, input().split())
maze = []
for i in range(m):
    maze.append(list(input()))

start = (0, 0)
goal = (m-1, n-1)

pathShortest = -1

Open = [(start, 0, None)]
Closed = {start}

while Open:
    O_TT = Open.pop(0)
    O = O_TT[0]

    if O == goal:
        if pathShortest == -1:
            pathShortest = O_TT[1]
        elif pathShortest > O_TT[-1]:
            pathShortest = O_TT[-1]

    for i in range(4):
        child = move(O, i, m, n)
        if child and child not in Closed:
            Open.append((child, O_TT[1] + 1, O_TT))
            Closed.add(child)

print(pathShortest)