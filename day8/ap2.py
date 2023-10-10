import pandas

sv = pandas.read_csv("dulieusinhvien.txt", sep=',',
                     header=None, names=['ma', 'ten', 'lop'])

lop = ['k18', 'k19']

sv1 = sv.query('lop in @lop')
print(sv1)
