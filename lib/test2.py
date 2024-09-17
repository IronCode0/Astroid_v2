import benchmark
from reg import reg as rr


class a(rr):
    def export_raw(self,addr="/",root=""):
        if root == "": root =self.main;
        if addr[0]=='/': addr = addr[1:]
        text = addr + "=" + str(root.val) + "\n"
        for c in root.children:
            text +=__class__.export_raw(self,addr+"/"+c,root.children[c])
        return text

    def import_raw(): pass


k=a()
#benchmark.reg.write_random(k,10)

k.write("LV/color",7)
k.write("LV/size/h",400)
k.write("LV/back",74)
k.write("RV/back",44)
k.write("LV/back/egege/gegege",77)
k.write("TS/back/egege/gegege",74)
k.write("TS/back/egege",74)
k.write("LV/for",5)
k.write("LV/size/w",600)
k.write("LV/color/force",999)

'''
=0
LV=0
LV/color=7
LV/color/force=999
LV/size=0
LV/size/h=400
LV/size/w=600
LV/back=74
LV/back/egege=0
LV/back/egege/gegege=77
LV/for=5
RV=0
RV/back=44
TS=0
TS/back=0
TS/back/egege=74
TS/back/egege/gegege=74

'''


#print(k.main.children)
print(k.export_raw())