def solution(food_times, k):
    def updateNumOfPlate(iterCnt):
        for key, value in list(numDict.items()):
            if value == iterCnt:
                del numDict[key]
        return len(numDict)

    numOfPlate = len(food_times)
    sortedTime = sorted(food_times)
    cur = 0  # sortedTime 커서
    numDict = {}
    for idx, i in enumerate(food_times):
        numDict[idx] = i
    iterCnt = 0

    while (sortedTime[cur] - iterCnt) * numOfPlate <= k:
        # print(f'{k}')
        k -= (sortedTime[cur] - iterCnt) * numOfPlate
        iterCnt = sortedTime[cur]
        while sortedTime[cur] == sortedTime[cur+1]:
            cur += 1
        cur += 1
        numOfPlate = updateNumOfPlate(iterCnt)
    answer = list(numDict.keys())[0]



    while numOfPlate <= k:
        print(f'dddd{k}')
        # 한줄 씩
        k -= numOfPlate
        iterCnt += 1
        numOfPlate = updateNumOfPlate(iterCnt)


    while k != 0:
        for key in list(numDict.keys()):
            if k == 0:
                answer = key
                break
            # print(f'하나씩 {k}')
            k -= 1
            numDict[key] -= 1
            if numDict[key] == iterCnt:
                del numDict[key]
    return answer + 1
# solution([7, 8, 3, 6, 7, 8, 5, 9, 11], 24)
# solution([3, 1, 2], 5)
# solution([124, 235, 346, 3453, 27, 43, 523, 45, 734, 634, 73, 423, 12, 23, 12, 41, 2241, 15], 3922)
for i in range(18, 24):
    print(f'---{i}---')
    print('다음', solution([3,3,5,5,3,5], i))
              # 2 2 4 4 2 4
              # 1 1 3 3 1 3
              # 0 0 2 2 0 2