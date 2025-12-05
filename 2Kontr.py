def Check(arr, direction):
    arrOld = list(map(int, arr))

    arrNew = []
    if direction == 1:
        for i in range(len(arrOld)):
            if arrOld[i] > 0:
                arrNew += [arrOld[i]]
    elif direction == -1:
        for i in range(len(arrOld)):
            if arrOld[i] < 0:
                arrNew += [arrOld[i]]
    else:
        for i in range(len(arrOld)):   
            if arrOld[i] == 0:
                arrNew += [arrOld[i]]
    return arrNew

def TestTask2():
    errorCount = 0
    testCases = [([1, -2, 3, 0, -5, 5], [1, 3, 5, 0, -2, -5]),
                ([0, 0, 0], [0, 0, 0]),
                ([-1, -2, -3], [-1, -2, -3]),
                ([5, 4, 3], [5, 4, 3]),
                ([1, -1, 0, 2, -2, 0], [1, 2, 0, 0, -1, -2])]
    for i in range(len(testCases)):
        excepted = testCases[i][1]
        if excepted != (Check(testCases[i][0], 1) + Check(testCases[i][0], 0) + Check(testCases[i][0], -1)):
            print(f"Error: result = {Check(testCases[i][0], 1) + Check(testCases[i][0], 0) + Check(testCases[i][0], -1)}, excepted = {excepted}")
            errorCount += 1
    if errorCount == 0:
        print("All tests passed")

TestTask2()