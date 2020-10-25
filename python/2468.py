import sys
import copy

m = int(sys.stdin.readline())
g = []
minH = 100
maxH = 0
for i in range(m):
    l = list(map(int, sys.stdin.readline().split()))
    g.append(l)
    minH = min(l) if min(l) < minH else minH
    maxH = max(l) if max(l) > maxH else maxH
def dfs(graph, i, j):
    stack = [[i, j]]
    while stack:
        x, y = stack.pop()
        graph[x][y] = 0
        adjacent = [[x-1, y], [x+1,y], [x, y-1], [x, y+1]]
        for aX, aY in adjacent:
            if 0 <= aX < len(graph) and 0 <= aY < len(graph) and graph[aX][aY] != 0:
                stack.append([aX, aY])

sol = []
for h in range(minH - 1, maxH):
    gr = copy.deepcopy(g)
    for j in range(m):
        for i in range(m):
            if 0 < gr[i][j] and gr[i][j] <= h:
                gr[i][j] = 0
    # print(h, gr)

    count = 0
    for j in range(m):
        for i in range(m):
            if gr[i][j] > 0:
                dfs(gr, i, j)
                count += 1
    sol.append(count)

print(max(sol))



