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