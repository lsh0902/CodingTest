N = int(input()) + 1
strN = list(str(N))
isPalin = True
while True:
    for i in range(len(strN) // 2):
        isPalin = True
        if strN[i] > strN[len(strN)-i-1]:
            strN[len(strN) - i - 1] = strN[i]
        elif strN[i] < strN[len(strN)-i-1]:
            strN[len(strN) - i - 1] = strN[i]
            N = int(''.join(strN)) + 10 ** (i + 1)
            strN = list(str(N))

        for i in range(len(strN) // 2):
            if strN[i] != strN[len(strN)-i-1]:
                isPalin = False
                break
        if isPalin: break
    if isPalin: break
    if len(strN) % 2 == 0: strN[len(strN) // 2] = strN[len(strN) // 2 - 1]
print(int(''.join(strN)))
