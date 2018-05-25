'''
【程序8】 题目:输出9*9口诀。 
1.程序分析:分行与列考虑,共9行9列,i控制行,j控制列。 
2.程序源代码:
'''
for a in range(1,10):
    for b in range(1,a+1):
        print('{0:2d} *{1:2d}={2:2d}'.format(b,a,a*b),end= ' ')
    print()
    