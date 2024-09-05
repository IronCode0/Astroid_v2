#import tkinter as tk
#from tkinter import ttk as ttk
#import ttkbootstrap as ttk

import UI
import threading
import tkthread; tkthread.patch()
import time

def File_viewer_GUI():
    FileUI = UI.FMUI()
    _nav_bar = FileUI.add_frame('nav'  , UI.FrameX('nav_ctrl'  , FileUI.window).pack(padx=5, pady=5, fill='x'))
    #_file_ex = FileUI.add_frame('file' , UI.FrameX('file_ex'   , FileUI.window).pack(padx=5, pady=0, fill='both', expand=True))
    #_sb_bar  = FileUI.add_frame('sb'   , UI.FrameX('Status_bar', FileUI.window).pack(padx=5, pady=0, fill='x'))
    print(type(_nav_bar.btn_bak.config(state='disable')))   #configure(state='disable')
    FileUI.GUI.start()

tkthread.call_nosync(File_viewer_GUI)

#temp = threading.Thread(target=File_viewer_GUI)
#temp.start()


# fill data
# nav btn
#print(type(_nav_bar.btn_bak.configure(state='disable')))
# nav adrr
# tree
# List
