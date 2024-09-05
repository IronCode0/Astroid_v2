import sys
import tkinter as tk
from tkinter import ttk
from random import choice
from lib import FShandle,debug

try:
    cmd_args =FShandle.Arg_Pharse(sys.argv)
except:
  debug.print("No Arguments")


def dataset():
    gdb = {
        'GUI':{
            'width':600,
            'height':400
        },
        'List':{
            'col':['Name','Date modified','Type','size']
        }
    }
    return gdb
gdb=dataset()
class fileGUI:
    def __init__(self,size=[gdb['GUI']['width'],gdb['GUI']['height']]):
        self.window=tk.Tk()
        self.window.geometry(size[0]+'x'+size[1])
        self.window.title("Files")
        # Nav bar
        # Tree
        # List
        self.window = ttk.Treeview(self.window,columns=gdb['List']['col'])
        # Status

      


