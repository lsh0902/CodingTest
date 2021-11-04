def solution(n, stations, w):
    answer = 0
    coverRange = 2 * w + 1
    underCover = []
    start = stations[0] - w
    end = stations[0] + w

    if start > 1: underCover.append([1, start])
    for i in range(1, len(stations)):
        curStart, curEnd = stations[i] - w, stations[i] + w
        if end + 1 < curStart: underCover.append([end + 1, curStart])
        end, start = curEnd, curStart
    if end < n: underCover.append([end + 1, n + 1])

    for i, j in underCover:
        myRange = j - i
        if myRange % coverRange:
            answer += myRange // coverRange + 1
        else:
            answer += myRange // coverRange

    return answer