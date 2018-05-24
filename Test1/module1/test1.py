for letter in 'Runoob': 
    if letter == 'o':
        pass
        print ('执行 pass 块')
    print ('当前字母 :', letter)
  
print ("Good bye!")

import sys
a = 'Runoob'
a = list(a)
it = iter(a)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
