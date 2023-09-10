# Mỗi trâu đứng ăn 5 bó cỏ nên tối đa số trâu đứng chỉ có thể là 100/5 tức là 20 con.
# Mỗi trâu nằm ăn 3 bó cỏ nên số trâu nằm nhỏ hơn hoặc bằng 100/3 tức là 33 con.
# Số trâu già = 100 - số trâu đứng - số trâu nằm.


for i in range(1, 21) :
    for j in range(1, 34) :
        k= 100 - i - j
        # print(k)
        if (5*i + 3*j + k/3 == 100):
            print( "Trâu đứng ",i," trâu nằm ",j," trâu già ",k)