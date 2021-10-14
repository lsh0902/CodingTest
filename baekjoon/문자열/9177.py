""" 실패 아직 못 품 """
import sys

def check(a, b, target):
    flag = [False for i in range(len(target))]
    lenA, lenB = len(a), len(b)
    cur = 0
    for idx, i in enumerate(target):
        if a[cur] == i:
            flag[idx] = True
            cur += 1
        if lenA == cur:
            break
    cur = 0
    for idx, i in enumerate(target):
        if not flag[idx]:
            if b[cur] == i:
                flag[idx] = True
                cur += 1
            if lenB == cur:
                break
    if False in flag:
        return False
    return True

input = sys.stdin.readline
N = int(input())
strs, ans = [], []

for i in range(N):
    strs.append(input().split())
for a, b, target in strs:
    if check(a, b, target):
        ans.append(True)
    else:
        ans.append(check(b, a, target))
for idx, i in enumerate(ans):
    if i: print(f'Data set {idx+1}: yes')
    else: print(f'Data set {idx + 1}: no')