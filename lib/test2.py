#import benchmark
#from test3 import reg
class Parent:
    def __init_subclass__(cls, **kwargs):
        def init_decorator(previous_init):
            def new_init(self, *args, **kwargs):
                previous_init(self, *args, **kwargs)
                if type(self) == cls:
                    self.__post_init__()
            return new_init

        cls.__init__ = init_decorator(cls.__init__)

    def __post_init__(self):
        pass
class a: _SIGN_HASH = 54886526
class d: _SIGN_HASH = 44659526
class reg:
    def __new__(cls,*args,**kwargs):
        if args[0]._SIGN_HASH == 44659526: return __class__
        else: return __class__.f_reg
    def __init__(): print("reg is __init__")
    class f_reg:
        def write(): pass
    def _func(*args): pass
    #def write(a,b,c): print('Write function')
    class write(Parent):
        def __init__(self,a,b,c):
            print("write is __init__")
            self.v=(a,b,c)
            self.n=1
        def __post_init__(self):
            print("_post_",self.v)
        def __del__(self): print(f'repeat = {self.n}',self.v);
        def repeat(self,n): self.n = n
            

a=reg(d()).write(4,7,8).repeat(4)
print('-------------------')
b=reg(d()).write(4,7,8)
print('-------------------')
print(type(a),type(b))
print("-----------------END-------------------")