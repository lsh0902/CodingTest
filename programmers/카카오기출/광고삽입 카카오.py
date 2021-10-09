def strToTime(str):
    str = str.split(':')
    return int(str[0]) * 3600 + int(str[1]) * 60 + int(str[2])

def timeToStr(time):
    h = time // 3600
    time = time % 3600
    m = time // 60
    sec = time % 60
    return f'{h:0{2}d}:{m:0{2}d}:{sec:0{2}d}'

def solution(play_time, adv_time, logs):
    play_time = strToTime(play_time)
    adv_time = strToTime(adv_time)
    timeArr = [0] * play_time
    logs = list(map(lambda x: x.split('-'), logs))
    for i in range(len(logs)):
        logs[i][0] = strToTime(logs[i][0])
        logs[i][1] = strToTime(logs[i][1])

    logLen = len(logs)
    logs = sorted(logs, key = lambda x: x[0])
    enter = list(map(lambda x : x[0], logs))
    out = list(map(lambda x: x[1], logs))
    enter.sort()
    out.sort()
    enter_cur = 0
    out_cur = 0
    viewer = 0
    for t in range(len(timeArr)):
        while enter_cur < logLen and t == enter[enter_cur] :
            viewer += 1
            enter_cur+=1

        while out_cur < logLen and t == out[out_cur]:
            viewer -= 1
            out_cur += 1
        timeArr[t] = viewer

    count = sum(timeArr[:adv_time])
    maxNum = count
    answer = 0
    l, r = 0, adv_time
    while r < play_time:
        count = count - timeArr[l] + timeArr[r]
        r += 1
        l += 1
        if count > maxNum:
            maxNum = count
            answer = l
    remainTime = adv_time - (play_time - answer)
    if remainTime > 0 :
        answer -= remainTime
    return timeToStr(answer)

print(solution(	"00:01:00", "00:00:10", ["00:00:00-00:00:10"]))

