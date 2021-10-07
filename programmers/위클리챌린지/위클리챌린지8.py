def solution(sizes):
    b, s = 0, 0
    for i, j in sizes:
        b = max(j, i) if max(j, i) > b else b
        s = min(i,j) if min(i,j) > s else s
    return b * s