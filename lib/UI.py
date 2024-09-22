import tkinter as tk
from tkinter import ttk as ttk
import debug
import importlib,importlib.util
import threading

def debug_list(n,list,default):
    try:
        return list[n]
    except:
        return default

class FMUI:
    def __init__(self,title='Window',size='400x300'):
        self.window =tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW",self.window.destroy)
        #print(type(self.window))
        self.window.title(title)
        self.window.geometry(size)
        self.window.minsize(150, 100)
        self.layout = 'pack'
        #self.nav_bar_items = ('C:','D:','E:','F:')
        #self.nav_bar_var= tk.StringVar(value=self.nav_bar_items[0])
        self.frames={}
        #self.GUI = threading.Thread(target=self.GUI_Thread)
    def add_frame(self,name,frame):
        if not name or not frame:
            print("can't add in list")
            return
        self.frames[name] =frame
        return frame
    def show(self):
        self.window.mainloop()
        #self.tr.start()
    def GUI_Thread(self):
        self.window.mainloop()

class _UI_NAV_BAR_:
    def __init__(self):
        self.frame = tk.Frame()
        self.btn_bak = ttk.Button(self.frame, text='<', width=3)
        self.btn_for = ttk.Button(self.frame, text='>', width=3)
        self.btn_up_ = ttk.Button(self.frame, text='^', width=3)
        self.btn_opt = ttk.Button(self.frame, text=':', width=3)
        self.var_nav = tk.StringVar()
        self.nav_bar = ttk.Combobox(self.frame,textvariable=self.var_nav)
        cb_list=()
        # pack
        self.btn_bak.pack(padx=2, pady=2, side='left')
        self.btn_for.pack(padx=2, pady=2, side='left')
        self.btn_up_.pack(padx=2, pady=2, side='left')
        self.nav_bar.pack(padx=2, pady=2, side='left', fill='x', expand=True)
        self.btn_opt.pack(padx=2, pady=2, side='left')
    def cout(self):
        print(self.t if hasattr(self,'t') else 'GG')
    def cb_list(self,text): self.nav_bar['values'] = text
    def cb_set(self,text): self.nav_bar.set(text)
    def pack(self,**Args):
        self.frame.pack(**Args)
        return self
class _CTRL_LV_AD_:
    def __init__(self):

        self.frame = tk.Frame()
        self.TV_ctrl = ttk.Treeview(self.frame)
        self.LV = LV(self.frame)
        #self.LV_ctrl = ttk.Treeview(self.frame)
        # pack
        self.TV_ctrl.pack(padx=2, pady=2, side='left', fill='y')
        self.LV.frame.pack(padx=2, pady=2, side='left', fill='both',expand=True)
        #store
    def pack(self,**Args):
        self.frame.pack(**Args)
        return self
class _CTRL_TV_AD_:
    pass
class _OBJ_BUTTON_:
    pass
class _UI_STA_BAR_:
    pass

class FrameX:
    _mlist={
        'nav bar' : "_UI_NAV_BAR_",
        'ListView': "_CTRL_LV_AD_",
        'TreeView': "_CTRL_TV_AD_",
        'Button'  : "_OBJ_BUTTON_",
        'Stat bar': "_UI_STA_BAR_",
    }
    _clist={
        '_UI_NAV_BAR_': _UI_NAV_BAR_,
        '_CTRL_LV_AD_': _CTRL_LV_AD_,
        '_CTRL_TV_AD_': _CTRL_TV_AD_,
        '_OBJ_BUTTON_': _OBJ_BUTTON_,
        '_UI_STA_BAR_': _UI_STA_BAR_,
    }
    def __new__(cls,_widget):
        if type(_widget) is str and (_widget in FrameX._clist or _widget in FrameX._mlist): return super().__new__(cls)
        if type(_widget) is not tuple: return None;
        try:
            importlib.import_module(_widget[0])
            if hasattr(importlib.import_module(_widget[0]),_widget[1]):
                t_class = getattr(importlib.import_module(_widget[0]),_widget[1])
                FrameX._mlist[t_class.RefID] = _widget[1]
                FrameX._clist[_widget[1]] = t_class
                return super().__new__(cls)
            else: debug.cout(f'Class: {_widget[1]} not found in module: {_widget[0]}');
        except ModuleNotFoundError:
            debug.cout(f"ERROR 0x400878: Module '{_widget[0]}' not found");
        return None;
    def __init__(self,widget,*args): self._module=FrameX.getcls(widget)(*args);
    def __getattr__(self,name): return getattr(self._module, name) if hasattr(self._module, name) else debug.dummy_func;
        
    @staticmethod
    def getcls(text):
        if type(text) is tuple: text = text[1]
        if text[0:1] != "_" and text in FrameX._mlist:
            text = FrameX._mlist[text]
        if text in FrameX._clist: return FrameX._clist[text]
        return debug.dummy_class
    def getfunc(module, name):
        if hasattr(module, name): return getattr(module, name) 
        else: return debug.dummy_func



class FrameX_2:
    def __init__(self,control,window):
        self.fill='none'
        self.expand=False
        self.frame = ttk.Frame(master = window)
        match(control):
            case 'nav_ctrl':
                self.navigation_bar(self.frame)
            case 'file_ex':
                self.file_ex(self.frame)
            case 'Status_bar':
                self.Status_bar(self.frame)
        #return self
    def navigation_bar(self,frame):
        self.frame = frame
        self.btn_bak = ttk.Button(self.frame, text='<', width=3)
        self.btn_for = ttk.Button(self.frame, text='>', width=3)
        self.btn_up_ = ttk.Button(self.frame, text='^', width=3)
        self.btn_opt = ttk.Button(self.frame, text=':', width=3)
        self.var_nav = tk.StringVar()
        self.nav_bar = ttk.Combobox(self.frame,textvariable=self.var_nav)
        # pack
        self.btn_bak.pack(padx=2, pady=2, side='left')
        self.btn_for.pack(padx=2, pady=2, side='left')
        self.btn_up_.pack(padx=2, pady=2, side='left')
        self.nav_bar.pack(padx=2, pady=2, side='left', fill='x', expand=True)
        self.btn_opt.pack(padx=2, pady=2, side='left')
        # store
        #self.obj=[self.frame,self.btn_bak, self.btn_for, self.btn_up_, self.btn_opt, self.nav_bar]
        #self.fill='x'
        #self.expand=False
    def file_ex(self,frame):
        self.frame = frame
        self.TV_ctrl = ttk.Treeview(self.frame)
        self.LV_ctrl = LV(self.frame)
        #self.LV_ctrl = ttk.Treeview(self.frame)
        # pack
        self.TV_ctrl.pack(padx=2, pady=2, side='left', fill='y')
        self.LV_ctrl.frame.pack(padx=2, pady=2, side='left', fill='both',expand=True)
        #store
        #self.obj=[self.TV_ctrl,self.LV_ctrl]
        #self.fill='both'
        #self.expand=True
    def Status_bar(self,frame):
        self.frame = frame
        self.SB_col1 = tk.Label(self.frame, text="Status Bar")
        self.SB_col1.pack(padx=2, pady=2, fill='x', expand=True)
        #self.fill='x'
        #self.expand=False
    def pack(self,**Args):
        self.frame.pack(**Args)
        return self

class LV:
    rlist=0
    def __init__(self,_frame):
        self.frame = tk.Frame(_frame,background='#828790') #background='#828790'
        self.style = ttk.Style()
        self.rlist=0
        self.LV_ctrl= ttk.Treeview(self.frame, show = 'headings',padding=2,style='Edge.Treeview')
        self.LV_ysb = ttk.Scrollbar(self.frame, orient="vertical", command=self.LV_ctrl.yview)
        self.LV_xsb = ttk.Scrollbar(self.frame, orient="horizontal", command=self.LV_ctrl.xview)
        self.LV_ctrl.configure(yscrollcommand=self.LV_ysb.set,xscrollcommand=self.LV_xsb.set)
        self.style.layout('Edge.Treeview',[('Edge.Treeview.treearea', {'sticky': 'nsew'})],)
        self.LV_ctrl.grid(row=0,column=0,padx=1,pady=1,sticky='news')
        self.LV_xsb.grid(row=1,column=0,sticky='ew')
        self.LV_ysb.grid(row=0,column=1,sticky='ns')
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.trigger()
        # <resume> text.bind('<Alt-KeyPress-a>',lambda event: print(event))
        # <resume> window.bind('<Motion>',lambda event: pos_var.set(f'x: {event.x} y: {event.y}'))

    def add(self,parent = '', index = 'end', values=""):
        if self.LV_ctrl.insert(parent = parent, index=index, values = values):
            self.rlist +=1
    def set_col(self,*col):
        self.LV_ctrl['columns'] = tuple(str(i) for i in range(len(col)))
        idx = 0
        for n in col:       #in range(len(col)):
            self.LV_ctrl.column(idx, width=debug_list(1,n,20), anchor=debug_list(2,n,'w'),stretch=False)
            self.LV_ctrl.heading(idx, text=debug_list(0,n,n[0]))
            idx +=1
    def 
    def getid(self): return self.frame;
    def update(self,raw):
        for i in range(len(raw)):
            self.add(values=raw[i])

#END