import sys
import copy

N = int(sys.stdin.readline().replace('\n', ''))
g = []
for i in range(N):
    g.append(list(map(int, list(sys.stdin.readline().replace('\n', '')))))

def dfs(graph, x, y):
    stack = [[x, y]]
    area = 0
    while stack:
        x, y = stack.pop()
        area += 1
        graph[x][y] = 0
        adjacent = [[x-1, y], [x+1,y], [x, y-1], [x, y+1]]
        for ax, ay in adjacent:
            if 0 <= ax < N and 0 <= ay < N and graph[ax][ay] == 1 and [ax, ay] not in stack:
                stack.append([ax, ay])
    return area

sol = []
solNum = 0

for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            area = dfs(g, i, j)
            sol.append(area)
            solNum += 1

print(solNum)
sol.sort()
for s in sol:
    print(s)