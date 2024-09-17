# record start time
import time
from sys import getsizeof as gs
import random
def debug_limit(input,min,max):
    if input < min:
        input= min
    if input > max:
        input = max
    return input

def benchmark(type,count,result,args):
    count = debug_limit(count,1,10)
    match type:
        case 'REG':
            pass
        case _:
            print("benchmark results")


class reg:
    def write(reg,interval=1,disp=False):
        if not reg: return;
        interval = debug_limit(interval,1,10)
        bm_write = 0
        time_start = time.perf_counter()
        while(time.perf_counter() - time_start < interval):
            __class__.write_random(reg)
            bm_write +=1
        if disp: print(f"Registry Benchmark Write: {int(bm_write/interval/10)}K/second")
        return (bm_write*100)
    def read(reg,interval=1,disp=0):
        if not reg: return;
        interval = debug_limit(interval,1,10)
        bm_read = 0
        time_start = time.perf_counter()
        while(time.perf_counter() - time_start < interval):
            __class__.read_random(reg)
            bm_read +=1
        if disp: print(f"Registry Benchmark Write: {int(bm_read/interval/10)}K/second")
        return (bm_read*100)
    def write_random(reg,count=100) -> 1:
        for _ in range(count): reg.write('/'.join([str(random.random()) for _ in range(3)]),random.random());
    def read_random(reg,count=100) -> 1:
        for _ in range(count): reg.read('/'.join([str(random.random()) for _ in range(3)]),random.random());
    def size(self,root=0): return __class__.size(self,self.main) if root == 0 else sum( [gs(root),gs(root.val),gs(root.children)] + [__class__.size(self,root.children[c]) for c in root.children ] )   
    def size2(self,root=0):
        if root == 0: root = self.main
        s = gs(root) + gs(root.val) + gs(root.children)
        for c in root.children: s += __class__.size(self,root.children[c]) 
        return s