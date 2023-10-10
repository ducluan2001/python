def chuoi(x):
    for i in range(len(x)):
        if (i == ' '):
            x[i + 1] = x.upper()
    print(x)


x = 'di me me'

chuoi(x)
