def cout(text):
    #do nothing
    print(text)
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