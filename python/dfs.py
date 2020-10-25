import sys

def dfs(graph, x, y):
    stack = [[x, y]]
    while stack:
        curX, curY = stack.pop()
        graph[curY][curX] = 0
        adjacent = [[curX-1,curY], [curX+1, curY], [curX, curY-1], [curX, curY+1], [curX-1, curY-1], [curX-1,curY+1], [curX+1, curY+1], [curX+1, curY-1]]
        for aX, aY in adjacent:
            if 0 <= aX < len(graph[0]) and 0 <= aY < len(graph) and graph[aY][aX] == 1:
                stack.append([aX, aY])

def solution(g, m, n):
    count = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                dfs(g, j, i)
                count += 1
    return count


sol = []
while True:
    line = list(map(int, sys.stdin.readline().split()))
    if len(line) == 2 and line[0] == 0 and line[1] == 0:
        break

    m, n = line
    g = []
    for i in range(n):
        g.append(list(map(int, sys.stdin.readline().split())))

    sol.append(solution(g, m, n))

for s in sol:
    print(s)

# 유기농배추
# sol = []
# T = int(input())
# for i in range(T):
#     m, n, cnt = map(int, sys.stdin.readline().split())
#     graph = [[0 for col in range(m)] for row in range(n)]
#     for c in range(cnt):
#         x, y = map(int, sys.stdin.readline().split())
#         graph[y][x] = 1

#     sol.append(solution(graph, m, n))

# for s in sol:
#     print(s)