""" 
定义一个集合的操作类：Setinfo 
 
包括的方法: 
 
1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型] 
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型] 
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型] 
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型] 
set_info =  Setinfo(你要操作的集合) 
"""  
class Setinfo(object):
    def __init__(self,my_Set):
        self.set = my_Set
    def add_setinfo(self,keyname):
        if keyname in self.set:
            return 'exit'
        elif isinstance(keyname, (str,int)):
            return self.set.add(keyname)
        else:
            return 'error'
    def get_intersection(self,unioninfo):
        if isinstance(unioninfo, set):
            return self.set & unioninfo
        return 'error'
    def get_union(self,unioninfo):
        if isinstance(unioninfo, set):
            return self.set | unioninfo
        return 'error'
    def del_difference(self,unioninfo):
        if isinstance(unioninfo, set):
            return self.set - unioninfo
        return 'error'
    
A = set([1, 2, 3, 4, 5, 2])  
B = set([5, 6, 3])  
set_info = Setinfo(A)  
print (set_info.add_setinfo('f')  )
print (set_info.get_intersection(B)  )
print (set_info.get_union(B)  )
print (set_info.del_difference(B) )