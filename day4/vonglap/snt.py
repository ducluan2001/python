import math

n = int(input())
ok = False

for i in range(2, int(math.sqrt(n) + 1)):
    if n % i == 0:
        ok = True
        break
if (not ok):
    print("day la so NT")
else:
    print("day k la so NT")
