global count
count=1000
import inspect
def trace_call():
    found=False
    lst=[]
    lst=[]
    for i in inspect.getouterframes( inspect.currentframe() ):
        #lst.append(str(i[3]) + ":" + str(i[2]))
        lst.append(i[3])
        #for j in i: print(j)
        #print("---------------")
    print("<trace",*[l for l in lst[len(lst)-1:1:-1]],sep=":",end=">")
       

def cout(text,id=0,trace=False):
    if id == 0:
        global count
        count = id = count+1
    
    if type(text) == str : print(f"<{id}:",text,">",sep="",end="")
    if type(text) == list: print(f"<{id}",*[t for t in text],sep=":",end=">")
    if type(text) == dict:
        i=0
        print(f"<{id}:__map__({len(text)})>",sep="",end="")
        trace_call()
        for e in text: print( f"\n  {e} : {text[e]}",end="")
    elif (trace):
        trace_call()
    print("")
    return 0

debug_code = {
    '110110':'COL_NOT_SET'
}

class dummy_class:
    def __init__(self,*args):
        cout('Creating a dummy class')
        if args: cout(args)
    def __getattr__(self,name):
        return dummy_func

def dummy_func(*args):
    cout('Calling a dummy function')
    if args: cout(args)


class cls():
    global debug_code
    def __init__(self,*args,**kwargs): self.args=args; self.kwargs=kwargs;
    def __getattribute__(self, attr):
        if attr.startswith('__'): return super().__getattribute__(attr)
        cls = self.__class__
        if attr in self.__dict__: return self.__dict__[attr]
        # Using [-2::-1] skips topmost one base classes, which will be ReverseLookup and object
        for base in cls.__mro__[-2::-1]:
            if attr in base.__dict__:
                value = base.__dict__[attr]
                # handle descriptors
                if hasattr(value, '__get__'): return value.__get__(self, cls)
                else: return value
        raise AttributeError("Attribute {} not found".format(attr))
    def __getattr__(self,name):
        self.__func__name__=name
        return name if callable(name) else self.__func__
    def __func__(self,*args,**kwargs):
        if debug_code: print(f"function '{self.__func__name__}' not found")
        return None
    def __getitem__(self, item):
        if type(item)==int: return self.args[item] if item < len(self.args) else None
        if type(item)==slice: return self.args[item]
        if item in locals(): return getattr(self,item)
        if item in self.kwargs: return self.kwargs[item]
        if hasattr(self,item): return getattr(self,item)
        return None
   
if __name__ =="__main__":
    class test(cls):
        def add(self,n):
            self.p=n
            return n+n

    t=test(7,4,5,7,6,8,9,7,1,4,r=41)
    print(t.add(4))
    print(t[0:4])

def balance(data,r=None,c=None):
    if not c: c=max([len(i) for i in data])
    if not r: r=len(data)
    for i in data:
        while len(i) < c: i.append(None)
        if len(i) > c: i=i[:c]
    while len(data) < r: data.append(None)
    if len(data) > c: data=data[:r]
    return data

def var(*args,gdefault=None):
    args=balance(args,c=4)
    def __TERMINATE__(a,b):
        print(f"invalid input {b} for varible {a}")
        return '__TERMINATE__'
    r={}
    for i in args:
        if (not i): continue
        if not i[0]: continue
        if type(i[2]) == list:
            if i[1] not in i[2]:
                if i[3]== '__TERMINATE__' or gdefault =='__TERMINATE__': __TERMINATE__(i[0],i[1])
                elif i[3]: i[1] == i[3]
                elif gdefault: i[1] == i[3]
                else: print(f'Unexpected Error <debug.var.for.default_data>')
        r[i[0]]=i[1]
    return r
        
