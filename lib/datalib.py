#incl
class arrayset:
    def __init__(self,n=[],dim=1):
        self.n = [list(map(int, i)) for i in n];  
        self.dim=dim   
        self.cur=0 
    def update(self,n): 
        self.n=[list(map(str, i)) for i in n]
        return self
    def comb(a,b):
        r=[]
        for i in a: r.extend([(i,j) for j in b])
        return tuple(r)  
    def padded(self):
        text=self.n
        cc=max(*[len(k) for k in text])
        (r,c)=(len(text),len(text[0]))
        cw=[0 for _ in range(cc)]
        for i in range(r):
            if len(text[i]) < cc: text[i].extend(["" for _ in range(cc-len(text[i]))])
        for i in range(cc): cw[i]=max(*[len(text[x][i]) for x in range(r)])
        #for i,j in comb(range(r),range(c)): text[i][j]+=" "*(cw[j]-len(text[i][j]))
        for i in range(r):
            for j in range(cc): text[i][j]+=" "*(cw[j]-len(text[i][j]))
        self.n = text
        return self;
    def reshape(self,*dim):
        if (len(dim) == 1 and self.dim ==1 ): return self;
        __class__.flatten(self)
        if   (len(dim) == 1): return self
        else: self.n=__class__._RS_SPT_(self,dim)
        return self;
    def _RS_SPT_(self,dim):
        if (len(dim)>1):
            r=[_ for _ in range(dim[0])]
            for i in range(dim[0]):
                r[i]=__class__._RS_SPT_(self,dim[1:])
            return r
        return [__class__.next(self) for _ in range(dim[0])]
    def next(self,default = None):
        if (self.cur >= len(self.n)): return self.n[-1] if default ==-1 else default;
        self.cur +=1
        return self.n[self.cur-1]
    def flatten(self):
        if self.dim==1: return;
        n=[]
        for k in self.n: n+=k
        self.n=n
        self.dim -=1
        if self.dim >1: __class__.flatten(self)
        return self;
    def raw(self): print(self.n)
    def show(self):
        r=self.n
        print('','-'*sum([3*len(r[0])+1,*[len(c) for c in r[0]]]))
        for i in r: print("",*[j for j in i],"",sep=" | ",end="\n "+'-'*sum([3*len(r[0])+1,*[len(c) for c in i]])+"\n" )
        return self
    def __add__(self,other): return self.n+other.n
    def __call__(self, *args, **kwds): __class__.show(self)
    def __repr__(self):
        t=""
        for i in self.n: t+= ' '.join(k for k in i) + "\n"
        return t;
class quick:
    def balance_2d(data,r,c):
        for i in range(r):
            if len(data[i]) == c: continue
            if type(data[i]) == tuple: data[i]=list(data[i])
            while len(data[i]) < c: data[i].append("")
    def pad2d(data,align=None):
        col_mlen=[len(i) for i in data]
        if sum(col_mlen)/len(col_mlen) != len(data[0]): __class__.balance_2d(data,len(data),max(col_mlen))
        col_w=[max([len(str(r[c])) for r in data]) for c in range(max(col_mlen))]
        r=len(data)
        c=len(col_w)
        if not align: align='L'*c
        toadd=''
        for i in range(r):
            if type(data[i]) == tuple: data[i]=list(data[i])
            for j in range(c):
                data[i][j] = str(data[i][j])
                if len(data[i][j]) == col_w[j]: continue
                toadd=" "*(col_w[j]-len(data[i][j]))
                if len(toadd) <1: continue
                if align[j]=='L': data[i][j]+=toadd
                if align[j]=='R': data[i][j]=toadd+data[i][j]
        return data

class datanest:
    def __init__(self,value=None) -> None: self.value=value
    def __setattr__(self, name: str, value) -> None: super().__setattr__(name,value if name=='value' else __class__(value))
    def __repr__(self) -> str: return str(super().__getattribute__('value'))

if __name__=="__main__":
    a=datanest()

    a.b=8
    a.b.c=10
    a.b.c.d=8
    a.b.d=12
    print(a, a.b, a.b.c)
    print(a.b[0], a.b.c[0])