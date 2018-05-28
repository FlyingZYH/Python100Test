""" 
定义一个列表的操作类：Listinfo 
 
包括的方法: 
 
1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型] 
2 列表元素取值：get_key(num) [num:整数类型] 
3 列表合并：update_list(list)      [list:列表类型] 
4 删除并且返回最后一个元素：del_key() 
 
list_info = Listinfo([44,222,111,333,454,'sss','333']) 
"""  
class Listinfo(object):
    def __init__(self,list):
        self.list = list
    def add_key(self,keyname):
        if isinstance(self.list, (str,int)):
            self.list.append(keyname)
            return self.list
        else :
            return 'error'
    def get_key(self,num):
        if num >= 0 and num <len(self.list):
            return self.list[num]
        else:
            return 'error'
    def update_list(self,list):
        return self.list.extend(list)
    def del_key(self):
        if len(self.list)>0:
            return self.list.pop(-1)
        else:
            return'error'
    
list_info = Listinfo([44, 222, 111, 333, 454, 'sss', '333'])  
print (list_info.add_key('1111')  )
print (list_info.get_key(4)  )
print (list_info.update_list(['1', '2', '3'])  )
print (list_info.del_key() )
        