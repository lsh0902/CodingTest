from collections import defaultdict
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    mydict = defaultdict(int)
    for i in range(N):
        arr = list(map(int, input().split()))
        for j in arr:
            mydict[j] += 1

    scores = sorted(list(set(mydict.values())))[-2]
    ans = []
    for i in mydict:
        if mydict[i] == scores:
            ans.append(i)
    ans.sort()
    for i in ans:
        print(i, end = ' ')
    print()

