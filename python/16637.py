import sys



for k in range((len(s)//2 + 1)//2):
    cnt = k
    while cnt > 0:
        idx = 0
        for i in range(idx, len(exp), 2):
            num1 = s[i]
