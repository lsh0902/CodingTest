import sys

def solution(line):
    def getCrossPoint(i, j):
        A, B, E = line[i]
        C, D, F = line[j]
        mo = A * D - B * C
        if mo == 0: return []
        x, y = (B * F - E * D) / mo, (E * C - A * F) / mo
        if x - int(x) or y - int(y): return []
        return [int(y), int(x)]

    points = []
    minX, minY, maxX, maxY = sys.maxsize, sys.maxsize, -sys.maxsize, -sys.maxsize
    for i in range(0, len(line) - 1):
        for j in range(i + 1, len(line)):
            point = getCrossPoint(i, j)
            if point:
                points.append(point)
                minX = min(minX, point[1])
                minY = min(minY, point[0])
                maxX = max(maxX, point[1])
                maxY = max(maxY, point[0])

    answer = [["." for i in range(maxX - minX + 1)] for j in range(maxY - minY + 1)]
    for y, x in points: answer[y - minY][x - minX] = "*"
    return list(map(lambda x: ''.join(x), answer))[::-1]
solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])