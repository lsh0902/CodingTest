def solution(n, m, x, y, queries):
    leftEnd, rightEnd = 0, m-1
    leftEndAmount, rightEndAmount = 1, 1
    YleftEnd, YrightEnd = 0, n-1
    YleftEndAmount, YrightEndAmount = 1, 1
    canAddValue = True
    YcanAddValue = True
    for orderNum, amount in queries:
        if orderNum == 0:
            leftEnd -= amount
            rightEnd -= amount

            if leftEnd < 0:
                if canAddValue:
                    leftEndAmount -= leftEnd
                leftEnd = 0
            if rightEnd < 0:
                if canAddValue:
                    rightEndAmount -= rightEnd
                rightEnd = 0
            if rightEnd == leftEnd:
                rightEndAmount = leftEndAmount
                canAddValue = False

        elif orderNum == 1:
            leftEnd += amount
            rightEnd += amount
            if leftEnd >= m:
                if canAddValue:
                    leftEndAmount += leftEnd - (m-1)
                leftEnd = m-1
            if rightEnd >= m:
                if canAddValue:
                    rightEndAmount += rightEnd - (m - 1)
                rightEnd = m-1
            if rightEnd == leftEnd:
                leftEndAmount = rightEndAmount
                canAddValue = False

        elif orderNum == 2:
            YleftEnd -= amount
            YrightEnd -= amount

            if YleftEnd < 0:
                if YcanAddValue:
                    YleftEndAmount -= YleftEnd
                YleftEnd = 0
            if YrightEnd < 0:
                if YcanAddValue:
                    YrightEndAmount -= YrightEnd
                YrightEnd = 0
            if YrightEnd == YleftEnd:
                YrightEndAmount = YleftEndAmount
                YcanAddValue = False

        elif orderNum == 3:
            YleftEnd += amount
            YrightEnd += amount
            if YleftEnd >= n:
                if YcanAddValue:
                    YleftEndAmount += YleftEnd - (n-1)
                YleftEnd = n-1
            if YrightEnd >= n:
                if YcanAddValue:
                    YrightEndAmount += YrightEnd - (n - 1)
                YrightEnd = n-1
            if YrightEnd == YleftEnd:
                YleftEndAmount = YrightEndAmount
                YcanAddValue = False


    X, Y = 0, 0
    if leftEnd == rightEnd:
        if y == leftEnd:
            X = m
    else:
        if leftEnd == y:
            X = leftEndAmount
        elif rightEnd == y:
            X = rightEndAmount
        elif leftEnd < y < rightEnd:
            X = 1

    if YleftEnd == YrightEnd:
        if x == YleftEnd:
            Y = n
    else:
        if YleftEnd == x:
            Y = YleftEndAmount
        elif YrightEnd == x:
            Y = YrightEndAmount
        elif YleftEnd < x < YrightEnd:
            Y = 1
    print(f'{leftEnd} : {leftEndAmount}, {rightEnd} : {rightEndAmount}')
    print(f'{YleftEnd} : {YleftEndAmount}, {YrightEnd} : {YrightEndAmount}')
    return X*Y
