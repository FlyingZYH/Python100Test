'''
【程序12】 题目:判断101-200之间有多少个素数,并输出所有素数。 
1.程序分析:判断素数的方法:用一个数分别去除2到sqrt(这个数),如果能被整除, 则表明此数不是素数,反之是素数。 
2.程序源代码:
'''
import math
def isprimy(a):
    d=[]
    for b in a:
        for c in range(2,int(math.sqrt(b))+1):
            if b % c == 0:
                d.append(b)
                break
    return d
b = []
for a in range(101,201):
    b.append(a)
for a in isprimy(b):
    b.remove(a)
print(b)
