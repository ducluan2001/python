f = open('data.txt', 'a')  # mo file de append
s = input()
f.writelines(s)
f = open('data.txt', 'r')  # mo file read
line = f.read()
print(line)
f.close()
