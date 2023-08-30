s = input("input a string: ")

res = ""

if len(s) < 2:
    s = ""
else:
    res = s[0: 2] + s[-2:]
    # res = s[0: 2] + s[len(s) - 2:]
print(res)
