'''
题目:输入某年某月某日,判断这一天是这一年的第几天?
1.程序分析:以3月5日为例,应该先把前两个月的加起来,然后再加上5天即本年的第几天,
     特殊 情况,闰年且输入月份大于3时需考虑多加一天。
2.程序源代码:
'''
day1 = [31,28,31,30,31,30,31,31,30,31,30,31]
day2 = [31,29,31,30,31,30,31,31,30,31,30,31]
allday =0
date = input("请输入年月日 格式为YY-MM-DD:")
date = date.split("-")
year = int(date[0])
month = int(date[1])
day= int(date[2])
if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0 :
    for a in range(month-1):
        allday += day2[a]
    allday += day
else:
    for a in range(month-1):
        allday += day1[a]
    allday += day
print(allday)