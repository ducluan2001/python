results = [['Thompson-Herah', 10.610],
           ['Fraser-Pryce', 10.740], ['Jackson', 10.760]]
for i, data in enumerate(results, start=0):
    name, time = data[0], data[1]
    print("{}. {} {}s".format(i, name, time))
