def sont(x):
    for i in range(2, x):
        if (x % i == 0):
            return False
    return True


for i in range(100):
    if (sont(i)):
        print(i, end=' ')
