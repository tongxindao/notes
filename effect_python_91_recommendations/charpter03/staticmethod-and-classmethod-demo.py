class A(object):
    def instance_method(self,x):   
        print("calling instance method instance_method(%s,%s)" % (self,x))
 
    @classmethod  
    def class_method(cls,x):  
        print("calling class_method(%s,%s)" % (cls,x)) 
 
    @staticmethod  
    def static_method(x):   
        print("calling static_method(%s)" % x)
    
a = A()
a.instance_method("test")
a.class_method("test")
a.static_method("test")
