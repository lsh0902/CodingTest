def solution(n, money):
    money.sort(reverse=True)

    def backtracking(idx, leftMoney):
        if idx == len(money)-1:
            if leftMoney % money[idx] == 0:
                return 1
        ret = 0
        cnt = 0
        while cnt * money[idx] <= leftMoney:
            ret += backtracking(idx + 1, leftMoney - cnt * money[idx])
            cnt += 1
        return ret

    return backtracking(0, n)
a=solution(5, [1,2,5])
print(a)