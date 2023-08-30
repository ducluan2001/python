s = "      For most Unix systems, you must download and compile the source code. The same source code archive can also be used to build the Windows and Mac versions, and is the starting point for ports to all other platforms.     "
print(s.count("s"))  # đếm số kí tự xuất hiện trong mảng

print(s.capitalize() + "capitalize")  # in hoa ký tự đầu tiên của chuỗi
print(s.upper() + "upper")  # in hoa tất cả các kí tự của chuỗi
print(s.lower() + "lower")  # in thường tất cả các kí tự của chuỗi
print(s.title() + "title")  # in hoa tất cả các kí tự ĐẦU của chuỗi
print(s.lstrip(" ") + "lstrip")  # xoá kí tự đầu chuỗi
print(s.strip(" ") + "strip")  # xoá kí tự ở đầu và cuối chuỗi
slip = s.split(" ", 15)
print(slip)  # tách chuỗi thành nhiều chuỗi con
s1 = slip
print("_".join(s1))  # nối chuỗi con thành 1 chuỗi bởi 1 kí tự
print(s.find("the", 60, ))  # tìm chuỗi con trong chuỗi trả về vị trí index
print(s.replace(" ", "_"))  # thay thế chuỗi con cũ thành chuỗi con khác
