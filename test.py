import sys
a = sys.stdin.readline().rstrip()
print(a)
[n, k] = list(map(int, a.split()))
# i = 0
# while i < a:
#     i += 1
#     x, y = map(int, sys.stdin.readline().rstrip().split())
#     print(x + y)

def erathos(n, k):
    arr = [n for n in range(2, n+1)]


    for a in arr:
        if a == 0:
            continue
        idx = arr.index(a)
        for i in range(idx, len(arr), a):
            if arr[i] == 0:
                continue
            if k == 1:
                return arr[i]
            arr[i] = 0
            k -= 1
            

    for p in list(filter(lambda x: x != 0, arr)):
        k -= 1
        if (k == 0):
            return p


print(erathos(n, k))