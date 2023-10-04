# ham tim max

def max(*a):  # con tro *a
    if (len(a) == 0):
        return
    else:
        max = a[0]
        for i in range(len(a)):
            if (max < a[i]):
                max = a[i]
    return max


print(max(1, 1, 2, 2, 3, 4, 5, 78, 7, 1, 7))
