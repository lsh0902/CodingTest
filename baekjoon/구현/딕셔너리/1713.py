num = int(input())
recommand = int(input())
arr = list(map(int, input().split()))
dic = {}
for idx, i in enumerate(arr):
    if i in dic:
        dic[i][0] += 1
    else:
        if len(dic) < num:
            dic[i] = [1, idx]
        else:
            cnt = sorted(list(set(map(lambda x : x[0], dic.values()))))[0]
            victim = []
            for j in dic:
                if dic[j][0] == cnt:
                    victim.append([j, dic[j][1]])
            victim.sort(key = lambda x : (x[1]))
            del dic[victim[0][0]]
            dic[i] = [1, idx]
for i in sorted(dic.keys()):
    print(i , end=" ")