import FShandle
from reg import reg
import datalib

reg_LV=reg.load.data('LV')
FShandle._SYS_FOLDER_(fileinfo=FShandle._SYS_FILE_CTRL_)    #may not require 

FS=FShandle.FS_Host(
    FShandle._SYS_FILE_CTRL_(),
    FShandle._SYS_FOLDER_(fileinfo=FShandle._SYS_FILE_CTRL_),
    FShandle._SYS_ROOT_DIR_(),
    FShandle._LNK_FAV_DIR_(),
    FShandle._SYS_RECYCLE_(),
    FShandle._SYS_W_DRIVE_(),  )

ds=datalib.arrayset()

print('kk',FS.m_obj['_SYS_FOLDER_'].fileinfo)
maxloop=0
while True and maxloop<50:
    maxloop+=1
    target=input()
    if target.upper()=='EXIT': break
    mname=FS.set(target)
    #_FS.set(mname)
    col_read = reg_LV[FS.target.__class__.__name__]['column_read']
    col_cout = reg_LV[FS.target.__class__.__name__]['column_cout']
    col_name = tuple(k[0] for k in col_cout)
    FS.set_col(*col_read)
    FS.read()
    #print(FS.target.data)
    ds.update(FS.cout(*col_name)).padded().show()
        

