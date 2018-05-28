'''
二：定义一个字典类：dictclass。完成下面的功能： 
dict = dictclass({你需要操作的字典对象}) 
1 删除某个key 
del_dict(key) 
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found" 
get_dict(key) 
3 返回键组成的列表：返回类型;(list) 
get_key() 
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list) 
update_dict({要合并的字典}) 
'''
class dictclass(object):
    def __init__(self,dict1):
        self.dict1 = dict1
    
    def del_dict(self,key):
        if key in self.dict1.keys():
            self.dict1.pop(key)
        else:
            return 'not found'
        
    def get_dict(self,key):
        if key in self.dict1.keys():
            return self.dict1[key]
        
    def get_key(self):
        return self.dict1.keys()
    
    def update_dict(self,dict2):
        self.dict1 = dict(self.dict1,**dict2)
        return self.dict1.values()

A = dictclass({'a': 1, 'b': 2}) 
print( A.get_dict('c')  )
print( A.del_dict('c')  )
print( A.get_key()  )
print( A.update_dict({'c': 3, 'd': 4})  )
        