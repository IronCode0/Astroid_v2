#import tkinter as tk
#from tkinter import ttk as ttk
#import ttkbootstrap as ttk

import UI
import threading
import time
import os
import debug
from FShandle import FS_Host
from reg import REG

reg_LV = REG.load.data('LV')

recent_folder = ("This PC","C:")

_FS = FS_Host()

def Thread_test(i):
    for i in range(i):
        time.sleep(1)
        print(i)

def File_viewer_GUI():
    FileUI = UI.FMUI('Main File Window','600x400')
    _nav_bar = FileUI.add_frame('_nav_bar'  , UI.FrameX('nav bar').pack(padx=5, pady=5, fill='x'))
    _file_ex = FileUI.add_frame('file' , UI.FrameX('ListView').pack(padx=5, pady=0, fill='both', expand=True))
    #_sb_bar  = FileUI.add_frame('sb'   , UI.FrameX('Status_bar').pack(padx=5, pady=0, fill='x'))
    
    FileUI.window.after_idle(FV_refresh,FileUI)
    FileUI.window.geometry()
    FileUI.show()
def FV_refresh(window,dir="This PC"):
    nav = window.frames['_nav_bar']
    nav.cb_list(recent_folder)
    nav.cb_set(dir)
    FV_Load(window,dir)

def FV_Load(window,dir):
    _FS.set('_SYS_W_DRIVE_')
    lv_col = reg_LV['_SYS_W_DRIVE_']['column']
    lv_cname = tuple(k[0] for k in lv_col)
    _FS.set_col(*lv_cname)
    _FS.read()
    #_FS.cout()
    window.frames['file'].LV.set_col(*lv_col)
    #_FS.getraw(*lv_cname)
    window.frames['file'].LV.update(_FS.getraw(*lv_cname))
    pass
    
 
temp = threading.Thread(target=File_viewer_GUI)
temp.start()

#Thread_test(3)


# fill data
# nav btn
#print(type(_nav_bar.btn_bak.configure(state='disable')))
# nav adrr
# tree
# List
