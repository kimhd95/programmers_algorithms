import sys
import copy

n, m, cnt = list(map(int, sys.stdin.readline().split()))
square = []
for c in range(cnt):
    sq = list(map(int, sys.stdin.readline().split()))
    square.append(sq)

g = [[1 for row in range(m)] for col in range(n)]
for s in square:
    for row in range(s[0], s[2]):
        for col in range(s[1], s[3]):
            g[n-col-1][row] = 0

def dfs(graph, i, j):
    stack = [[i, j]]
    area = 0
    while stack:
        x, y = stack.pop()
        area += 1
        # print(x, y, area)
        graph[x][y] = 0
        adjacent = [[x-1, y], [x+1,y], [x, y-1], [x, y+1]]
        for aX, aY in adjacent:
            if 0 <= aX < len(graph) and 0 <= aY < len(graph[0]) and graph[aX][aY] == 1 and [aX, aY] not in stack:
                stack.append([aX, aY])
    return area

sol = []
solNum = 0
# print(g)
for i in range(m):
    for j in range(n):
        if g[j][i] == 1:
            area = dfs(g, j, i)
            sol.append(area)
            solNum += 1
            # print(g)

print(solNum)
sol.sort()
print(' '.join(list(map(str, sol))))