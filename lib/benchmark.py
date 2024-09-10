# record start time
import time
import sys
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
            from reg import REG
            bm_reg(REG,args[0],args[1],count,result)
        case _:
            print("benchmark results")



def bm_reg(src,type='A',interval=1,count=1,result=0):
    interval = debug_limit(interval,1,10)
    result = debug_limit(result,0,1)
    if (type == 'M'):
        output = bm_reg_mem_usage(src.main) + sys.getsizeof(src.main) + sys.getsizeof(src)
        if result == 1: print(f"memory usage {output}")
        return output
    print(f"Expected time {interval*2*count}")
    r = [0,0]
    for x in range(0,count):
        try:
            temp = src()
        except:
            print("Can't find targed code to benchmark")
            return
        bm_read = 0
        bm_write = 0
        if (type == 'A' or type == 'W' ):
            time_start = time.perf_counter()
            while(time.perf_counter() - time_start < interval):
                temp.write("LV/color",7)
                temp.write("LV/size/h",400)
                temp.write("LV/back",74)
                temp.write("RV/back",44)
                temp.write("LV/back/egege/gegege",77)
                temp.write("TS/back/egege/gegege",74)
                temp.write("TS/back/egege",74)
                temp.write("LV/for",5)
                temp.write("LV/size/w",600)
                temp.write("LV/color/force",999)
                bm_write +=1
        if (type == 'A' or type == 'R' ):
            time_start = time.perf_counter()
            while(time.perf_counter() - time_start < interval):
                temp.read("LV/color")
                temp.read("LV/size/h")
                temp.read("LV/back")
                temp.read("RV/back")
                temp.read("LV/back/egege/gegege")
                temp.read("TS/back/egege/gegege")
                temp.read("TS/back/egege")
                temp.read("LV/for")
                temp.read("LV/size/w")
                temp.read("LV/color/force")
                bm_read +=1
        
        r[0] +=bm_write
        r[1] +=bm_read
    print(f"Registry Benchmark Results")
    if result == 1:
        if (type == 'A' or type == 'W' ): print(f"Registry Write {int(bm_write/count/interval/100)}K/second");
        if (type == 'A' or type == 'R' ): print(f"Registry Read {int(bm_read/count/interval/100)}K/second");
    #print(sys.getsizeof(src))
    return (bm_write/count,bm_read/count) 

def bm_reg_mem_usage(loc,p=0):
    #dump(REG.main)
    sum =sys.getsizeof(loc)
    if p == 1: print(loc.val);
    for n in loc.children:
        sum +=bm_reg_mem_usage(loc.children[n])
    return sum
