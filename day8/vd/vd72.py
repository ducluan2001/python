f = open('data.txt', 'a')  # mo file append
s = input()
# f.write(s)
f.writelines(s)
f.close()
