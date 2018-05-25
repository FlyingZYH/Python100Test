'''
【程序9】 题目:要求输出国际象棋棋盘。
 1.程序分析:用i控制行,j来控制列,根据i+j的和的变化来控制输出黑方格,还是白方格。
 2.程序源代码:
'''
for a in range(8):
    for b in range(8):
        if (a + b) % 2 == 0:
            print(0,end=' ')
        else:
            print(1,end =' ')
    print() 