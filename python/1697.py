import sys

n, k = map(int, sys.stdin.readline().split())

visited = dict()

queue = [n]
visited[n] = 0
while queue:
    # print(queue)
    pos = queue.pop(0)
    if pos == k:
        print(visited[k])
        break

    cpos = [pos-1, pos+1, pos*2]
    for c in cpos:
        if c not in visited.keys() and c > 0:
            if visited.get(c) and visited[c]
            visited[c] = visited[pos] + 1
            if c not in queue and not (c == pos*2 and c > 2*k): 
                queue.append(c)

