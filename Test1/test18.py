""" 
题目一： 写一个网页数据操作类。完成下面的功能： 
 
提示：需要用到urllib模块 
 
get_httpcode()获取网页的状态码，返回结果例如：200,301,404等 类型为int 
 
get_htmlcontent() 获取网页的内容。返回类型:str 
 
get_linknum()计算网页的链接数目。 
 
"""  
from urllib import request
class page_data(object):
    def __init__(self,add_url):
        self.url = add_url
        self.status = request.urlopen(self.url).getcode()
        self.content = request.urlopen(self.url).read().decode('utf-8')
    def get_httpcode(self):
        return self.status
    def get_htmlcontent(self):
        return self.content
    def get_linknum(self):
        return len(self.content.split('<a href=')) - 1  
    
A = page_data("http://www.baidu.com")  
print( A.get_httpcode()  )
print( A.get_htmlcontent())  
print( A.get_linknum() )
    