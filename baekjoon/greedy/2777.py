"""
숫자놀이
"""

N = int(input())
nums = [int(input()) for i in range(N)]
for num in nums:
    if num == 1:
        print(1)
        continue

    answer = 0
    while num != 1:
        flag = True
        for i in range(9,1,-1):
            if num % i == 0:
                num /= i
                answer += 1
                flag = False
                break
        if flag:
            answer = -1
            break
    print(answer)