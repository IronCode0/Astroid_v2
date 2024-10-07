import debug
#import importlib
#import importlib.util
class pseudo_class:
    def __init__(self,*objects):
        self.target = False
        self.m_obj={}
        for k in objects: self.add(k)
    def __getattr__(self, name: str):
        if hasattr(self.target, name): return getattr(self.target, name) 
        else: return debug.cout('Attribute does not exit')
    def __repr__(self) -> str:
        return str(f"{self.target}\nName={self.target.__class__.__name__}")
    def add(self,module):
        if (type(module)==tuple): debug.cout("Feature not available")
            #if temp_module is not None: self.m_obj[module_str] = self.target = temp_module()
            #elif importlib.util.find_spec(module_str):
            #    self._mlist[module_str] = self._module = importlib.import_module(module_str)(*args)
            #else: print('error 0x400878: module does not found')
        if (type(module.__class__) !=type): return self;
        self.m_obj[module.__class__.__name__]=module
        return self
    def set(self,target):
        flag=False
        if target in self.m_obj:
            flag=True
            self.target=self.m_obj[target]
        else:
            for m in self.m_obj:
                if not callable(self.m_obj[m].check_support): continue;
                if self.m_obj[m].check_support(target):
                    self.target=self.m_obj[m]
                    flag=True
                    break
        if flag and hasattr(self.target,'_update'): self.target._update(target)
        return self
    def select(self,idx):
        (t_module,args)=self._module._select(idx)
        if not self._module.__class__.__name__ == t_module: self.set(t_module)
        for key in args:
            if hasattr(self._module, key): getattr(self._module, key)(args[key])
    def cout(self,*Args):
        if not hasattr(self.target,'data'): return None
        r=[]
        for n in self.target.data: r.append([n[self.target._cols[a]] for a in Args]);
        return r 
