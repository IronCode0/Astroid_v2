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

