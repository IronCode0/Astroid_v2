class reg:
    def __init__(self): self.val = 0; self.main = self.Node(0);
    def write(self,addr,value):
        if addr == "": return 0
        loc = self.main
        for n in addr.split("/"):
            if n not in loc.children: loc.add(n,self.Node())
            loc = loc.children[n]
        loc.val = value
    def read(self,addr):
        if addr == "": return 0
        loc = self.main
        for n in addr.split("/"):
            if n not in loc.children: return 0
            loc = loc.children[n]
        return loc.val
    def set_raw(self,raw,root=None):
        if not root: root = self.main;
        p=0
        l= len(raw)
        brc = 0
        while p < l:
            if raw[p] == "<":
                brc +=1
                s1=p
                while not raw[s1] == "=": s1 +=1
                key = raw[p+1:s1]
                s2 = s1
                while s2 < l:
                    s2 +=1
                    if raw[s2] == "<": break #new
                    if raw[s2] == ">": break;
                val = raw[s1+1:s2]
                #print(key,val)
                root.children[key] = self.Node(val)
                #print( root.children[key])
                if raw[s2] == "<": 
                    end = 0
                    t=l-1
                    while end != brc:
                        if raw[t] == ">": end +=1;
                    p = self.set_raw(raw[s2:end],root.children[key]);
            p += 1
            if raw[p] == ">": brc-= 1;
            if brc == 0: break;
        return p
    def get_raw(self):
        text= __class__._rec_phrase(self.main)
        return text
    def _rec_phrase(addr):
        #print(addr.children)
        text = ""
        if not addr.children: return text
        for e in addr.children:
            print(e)
            child = addr.children[e]
            text +="<"+ e + "=" + str(child.val) + __class__._rec_phrase(child) + ">"
        return text
    class Node:
        def __init__(self,value = 0) -> None: self.val = value; self.children = {};
        def add(self,param,child): self.children[param] = child; return child
        def get(self,param): return self.children[param]
'''


t = reg()
util.write_random(t)
import time
time_start = time.perf_counter()
s=t.size()
time_end = time.perf_counter()
print(f'calc size in {time_end} for {t} bytes using one line')
time_start = time.perf_counter()
s=t.size2()
time_end = time.perf_counter()
print(f'calc size in {time_end} for {t} bytes using multiple line')

t.write("LV/color",7)
t.write("LV/size/h",400)
t.write("LV/back",74)
t.write("RV/back",44)
t.write("LV/back/egege/gegege",77)
t.write("TS/back/egege/gegege",74)
t.write("TS/back/egege",74)
t.write("LV/for",5)
t.write("LV/size/w",600)
t.write("LV/color/force",999)

print(t.read("LV/size/h"))
print(t.save_file())
'''



#raw="<LV=0<color=7<force=999>><size=0<h=400><w=600>><back=74<egege=0<gegege=77>>><for=5>><RV=0<back=44>><TS=0<back=0<egege=74<gegege=74>>>>"



