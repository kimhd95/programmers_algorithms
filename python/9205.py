import sys

T = int(sys.stdin.readline())

def getDistance(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

emos = []
for _ in range(T):
    marketCnt = int(sys.stdin.readline())
    curPos = list(map(int, sys.stdin.readline().split()))
    marketsPos = []
    for __ in range(marketCnt):
        marketsPos.append(list(map(int, sys.stdin.readline().split())))
    endPos = list(map(int, sys.stdin.readline().split()))

    queue = [curPos]
    visited = []
    emo = "sad"
    while queue:
        pos = queue.pop()
        visited.append(pos)
        if pos == endPos:
            emo = "happy"
            break

        for m in marketsPos+[endPos]:
            if getDistance(pos, m) <= 1000 and m not in visited:
                queue.append(m)
    emos.append(emo)

for e in emos:
    print(e)
        

