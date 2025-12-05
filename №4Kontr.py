import random

# 4
def pribav(povt):
    global chislo
    if abs(povt) == 0:
        direction = 1
    else:
        direction = abs(povt) / povt
    if direction == 1:
        for i in range(0, povt):
            chislo += 1
    else:
        povt = abs(povt)
        for i in range(povt, 0, -1):
            chislo -= 1


def TestTask1():
    errorCount = 0
    for x in range(-10, 11):
        for y in range(-10, 11):
            u = (x, y)
            # print(*u)
            excepted = x + y
            if Task1(*u) != excepted:
                print(f"Error: m = {x}, n = {y}, result = {Task1(*u)}, excepted = {excepted}")
                errorCount += 1
    if errorCount == 0:
        print("All tests passed")

        


def Task1(m, n):

    global chislo
    chislo = 0
    pribav(m)
    pribav(n)
    return chislo


TestTask1()