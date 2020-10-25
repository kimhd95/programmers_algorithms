import sys
import copy

n, m = list(map(int, sys.stdin.readline().split()))
g = []
for i in range(n):
    g.append(list(map(int, list(sys.stdin.readline().replace('\n', '')))))

def bfs(graph, x, y):
    queue = [[x, y]]
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    while queue:
        x, y = queue.pop(0)
        if x == m-1 and y == n-1:
            return visited[y][x]

        adjacent = [[x-1, y], [x+1,y], [x, y-1], [x, y+1]]
        for aX, aY in adjacent:
            if 0 <= aX < m and 0 <= aY < n:
                if graph[aY][aX] == 1 and visited[aY][aX] == 0:
                    visited[aY][aX] = visited[y][x] + 1
                    queue.append([aX, aY])

print(bfs(g, 0, 0))