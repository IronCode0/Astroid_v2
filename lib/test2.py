'''
import importlib
import importlib.util
import debug
_FS_ = ('_SYS_FOLDER_','_SYS_ROOT_DIR_','_SYS_RECYCLE_','_LNK_FAV_DIR_')

class _SYS_FOLDER_:
    def __init__(self): self.value = '_SYS_FOLDER_';
class _SYS_ROOT_DIR_:
    def __init__(self): self.value = '_SYS_ROOT_DIR_';
class _SYS_RECYCLE_:
    def __init__(self): self.value = '_SYS_RECYCLE_';

'''

import os ,time
from FShandle import file, FS_Host
from reg import REG as REG
f = 'F:\\Folder\\Astroid_v2\\temp\\test_file.docx'
d = 'F:\\Folder\\Astroid_v2'

db = FS_Host('_SYS_ROOT_DIR_',d)
file.load_reg(REG)
db.set_col('FullName', 'NameNoExt', 'ExtOnly', 'EO_format', 'DateModified', 'DM_format', 'ByteSize', 'BS_format')
db.read()
db.cout('Group','BS_format','EO_format')

'''
db = folder(d)

file.load_reg(REG)
db.set_col('FullName', 'NameNoExt', 'ExtOnly', 'EO_format', 'DateModified', 'DM_format', 'ByteSize', 'BS_format')
db.read()
db.print('Group','BS_format','EO_format')
'''

