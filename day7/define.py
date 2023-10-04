# to hop chap k cua n
# c = n! / k!*(n-k)!

def giaiThua(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


def main():
    print(giaiThua(5) / (giaiThua(2) * giaiThua(5 - 2)))


main()
