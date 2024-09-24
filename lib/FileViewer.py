#import tkinter as tk
#from tkinter import ttk as ttk
#import ttkbootstrap as ttk

import UI
import threading
import time
import os
import debug
from FShandle import FS_Host
from reg import reg as REG

reg_LV = REG.load.data('LV')

recent_folder = ("This PC","C:")





def EX_FILE_VIEW():
    gui=UI.FMUI()

def File_viewer_GUI(id,dir):
    _FS = FS_Host()
    FileUI = UI.FMUI('Main File Window','600x400')
    _nav_bar = FileUI.add_frame('_nav_bar'  , UI.FrameX('nav bar').pack(padx=5, pady=5, fill='x'))
    _file_ex = FileUI.add_frame('file' , UI.FrameX('ListView').pack(padx=5, pady=0, fill='both', expand=True))
    #_sb_bar  = FileUI.add_frame('sb'   , UI.FrameX('Status_bar').pack(padx=5, pady=0, fill='x'))
    # <resume> _file_ex.frames[_nav_bar].LV.trigger()
    FileUI.window.after_idle(FV_refresh,FileUI,_FS,dir)
    FileUI.window.geometry()
    FileUI.show()
def FV_refresh(window,_FS,dir="This PC"):
    nav = window.frames['_nav_bar']
    nav.cb_list(recent_folder)
    nav.cb_set(dir)
    FV_Load(window,_FS,dir)

def FV_Load(window,_FS,dir):
    
    mname=_FS.set(dir)
    #_FS.set(mname)
    lv_col = reg_LV[mname]['column']
    lv_cname = tuple(k[0] for k in lv_col)
    #print(lv_col,lv_cname)
    #_FS.set_col(*lv_cname)
    _FS.read(self=_FS)
    #_FS.cout()
    window.frames['file'].LV.set_col(*lv_col)
    #_FS.getraw(*lv_cname)
    window.frames['file'].LV.update(_FS.getraw(*lv_cname))
    pass
    
 
#Thread_test(3)
class process:
    _list=[]
    _cur =0
    t=""
    def __init__(self,time) -> None:
        self.ID={};
        self.data={"s_time":0,"e_time":0,"clock":0}
        t=time
    def add(self,thread=None):
        #print(type(thread.__class__),type(threading.Thread.__class__))
        if type(thread.__class__) == type:  __class__._list.append(thread)
        elif type(thread) in (list,tuple): [__class__._list.append(t) for t in thread]
        return self
    def start(self,id=-1):
        if (self.data["s_time"]==0): self.data['s_time']=time.perf_counter()
        if (id !=-1): __class__._list[id].start()
        else: [i.start() for i in __class__._list]
        return self
    def join(self):
        for i in __class__._list:
            try: i.join()
            except RuntimeError: print("cannot join thread before it is started")
        self.data["clock"]=__class__.t.perf_counter()-self.data["s_time"]
        return self;
    def thread_list(self):
        print(__class__._list)
        return self
    def __setitem__(self, key, value):  
        self.data[key]=value
    def __getitem__(self, key): return  self.data[key]
    @staticmethod
    def next():
        __class__._cur +=1
        return __class__._cur
#main = process()
main=process(
        time=time
    ).add(
        threading.Thread(target=File_viewer_GUI,args=("0x002","This PC"))
    ).thread_list().start().join()



# fill data
# nav btn
#print(type(_nav_bar.btn_bak.configure(state='disable')))
# nav adrr
# tree
# List
