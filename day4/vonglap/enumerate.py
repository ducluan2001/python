results = [['Thompson-Herah', 10.610],
           ['Fraser-Pryce', 10.740], ['Jackson', 10.760]]
for i, data in enumerate(results, start=2):
    name, time = data[0], data[1]
    print("{}. {} {}s".format(i, name, time))
# với i là chỉ số index và data nằm trong danh sách
# enumerate(danh sách, bắt đầu từ)
# chạy ví dụ để hiểu thêm
