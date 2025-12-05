def LongestWord(lineS):
    arrW = lineS.split()
    longW = ""
    for curW in arrW:
        if len(curW) > len(longW):
            longW = curW
    return longW

def TestTask3():
    errorCount = 0
    testCases = [("NEWTEST NEW TEST N E W T E S T", "NEWTEST"),
                 ("short word mediumword LONGESTWORD", "LONGESTWORD"),
                 ("1 2 3 five 6 7 8 9 10", "five"),
                 ("singleword", "singleword"),
                 ("", "")]
    for i in range(len(testCases)):
        excepted = testCases[i][1]
        if excepted != LongestWord(testCases[i][0]):
            print(f"Error: result = {LongestWord(testCases[i][0])}, excepted = {excepted}")
            errorCount += 1
    if errorCount == 0:
        print("All tests passed")

TestTask3()