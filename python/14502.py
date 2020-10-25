import sys
import copy


def bfs(m, start):
    queue = [start]
    visited = [start]
    while queue:
        x, y = queue.pop(0)
        m[y][x] = 22
        apos = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
        for ax, ay in apos:
            if 0 <= ax < len(m[0]) and 0 <= ay < len(m) and [ax, ay] not in visited:
                visited.append([ax, ay])
                if m[ay][ax] == 0 or m[ay][ax] == 2:
                    queue.append([ax, ay])

def spreadVirus(m):
    for j in range(len(m)):
        for i in range(len(m[0])):
            if m[j][i] == 2:
                bfs(m, [i, j])


n, m = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

walls = []
for j1 in range(n):
    for i1 in range(m):
        if matrix[j1][i1] == 0:
            for j2 in range(j1, n):
                for i2 in range(m):
                    if j2 == j1 and i2 <= i1 or matrix[j2][i2] != 0: continue
                    for j3 in range(j2, n):
                        for i3 in range(m):
                            if j3 == j2 and i3 <= i2 or matrix[j3][i3] != 0: continue
                            walls.append([[i1, j1], [i2, j2], [i3, j3]])

counts = []
for ws in walls:
    newMatrix = copy.deepcopy(matrix)
    for w in ws:
        newMatrix[w[1]][w[0]] = 1
    
    spreadVirus(newMatrix)

    count = 0
    for j in range(n):
        for i in range(m):
            if newMatrix[j][i] == 0: count += 1
    counts.append(count)

print(max(counts))
