import os, time, debug
import importlib
import importlib.util



class FS_Host:
    def __init__(self,module=False,*args):
        self._module = False
        self._mlist={}
        if module: self.set(module,*args)
    def __getattr__(self, name: str):
        if hasattr(self._module, name): return getattr(self._module, name) 
        else: return debug.cout('Attribute does not exit')
    def set(self,module,*args):
        if module in self._mlist: self._module = self._mlist[module]
        else:
            temp_module = globals().get(module)
            if temp_module is not None: self._mlist[module] = self._module = temp_module()
            elif importlib.util.find_spec(module): self._mlist[module] = self._module = importlib.import_module(module)(*args)
            else: print('error 0x400878: module does not found')
    def select(self,idx):
        (t_module,args)=self._module._select(idx)
        if not self._module.__class__.__name__ == t_module:
            self.set(t_module)
            print(77)
        for key in args:
            if hasattr(self._module, key): getattr(self._module, key)(args[key])
    
class _SYS_FILE_CTRL_:
    '''
    getinfo Args:
    FullName, NameNoExt, ExtOnly, EO_format, FileDir, FileDrive, DateModified, DateM_format,
    DateCreated,DC_format, DateAccessed, DA_format, ByteSize, BS_format, DiskSize
    '''
    _Type = {} #REG.load.FileType()
    _cols = {
        'FullName'      :  0, 'NameNoExt'    :  1, 'ExtOnly'    :  2, 'EO_format'   :  3, 'FileDir'   : 4, 'FileDrive'    : 5,
        'FileAttribute' :  6, 'DateModified' :  7, 'DM_format'  :  8, 'DateCreated' :  9, 'DC_format' : 10,'DateAccessed' : 11,
        'DA_format'     : 12, 'ByteSize'     : 13, 'BS_format'  : 14, 'DiskSize'    : 15, 'Group'     : 16
        }
    _default_col = tuple((True,*(False for n in range(len(_cols)-1))))
    @staticmethod
    def load_reg(REG): _SYS_FILE_CTRL_._Type = REG.load.FileType();
    def splitpath(_file=""):
        if (not _file): return 0;
        (_path,_name) = os.path.split(_file)
        (_name,_ext) = os.path.splitext(_name)
        return tuple((_path[0:1],_path,_name,_ext[1:]))
    def getinfo(_file="",args=_default_col):
        if (not _file): return 0;
        temp=[*args]
        (_drive,_path,_name,_ext) = _SYS_FILE_CTRL_.splitpath(_file)
        if os.path.isdir(_file):
            if args[0] : temp[0]  = str(_name + ("." + _ext if _ext else ""));   # FullName
            if args[1] : temp[1]  = temp[0];                                # NameNoExt
            if args[3] : temp[3]  = "File Folder";                          # EO_format
            if args[7] : temp[7]  = os.path.getmtime(_file);                # DateModified
            if args[8] : temp[8]  = time.ctime(os.path.getmtime(_file));    # DM_format
            if args[9] : temp[9]  = os.path.getctime(_file);                # DateCreated
            if args[10]: temp[10] = time.ctime(os.path.getctime(_file));    # DC_format
            if args[11]: temp[11] = os.path.getatime(_file);                # DateAccessed
            if args[12]: temp[12] = time.ctime(os.path.getatime(_file));    # DA_format
            temp[2]  = 'Folder';   # ExtOnly
            if args[4]: temp[4]  = _path;   # FileDir
            if args[5]: temp[5]  = _drive;   # FileDrive
            temp[6]  = False;   # FileAttribute
            temp[13] = int(0);   # ByteSize
            temp[14] = int(0);   # BS_format
            temp[15] = int(0);   # DiskSize
            temp[16] = '_FOLDER'
            return temp
        if (not os.path.isfile(_file)): return 0;
        ts = os.path.getsize(_file)
        if args[0] : temp[0]  = str(_name + ("." + _ext if _ext else ""));   # FullName
        if args[1] : temp[1]  = _name;                                  # NameNoExt
        if args[2] : temp[2]  = str(_ext if _ext else 'File');          # ExtOnly
        if args[3] : temp[3]  = _SYS_FILE_CTRL_._Type[_ext.lower()] if _ext.lower() in _SYS_FILE_CTRL_._Type else (_ext.upper() + " File");    #EO_format
        if args[4] : temp[4]  = False;                                  # FileDir
        if args[5] : temp[5]  = False;                                  # FileDrive
        if args[6] : temp[6]  = False;                                  # FileAttribute
        if args[7] : temp[7]  = os.path.getmtime(_file);                # DateModified
        if args[8] : temp[8]  = time.ctime(os.path.getmtime(_file));    # DM_format
        if args[9] : temp[9]  = os.path.getctime(_file);                # DateCreated
        if args[10]: temp[10] = time.ctime(os.path.getctime(_file));    # DC_format
        if args[11]: temp[11] = os.path.getatime(_file);                # DateAccessed
        if args[12]: temp[12] = time.ctime(os.path.getatime(_file));    # DA_format
        if args[13]: temp[13] = ts;                        # ByteSize
        if args[14]: temp[14] = misc.data_size(ts,'A',True);    # BS_format
        if args[15]: temp[15] = ts;                        # DiskSize
        temp[16] = '_FILE'
        return temp
class _SYS_FOLDER_:
    def __init__(self,path=""):
        self.column = ()
        self.reset_col()
        self.set_col('FullName')
        self.data=[]
        self.group='DEFAULT'
        self.grp_lst = ()
        if path: self.set_path(path)
    def set_path(self,path):
        temp=path if not path[-1:] == "\\" else path[0:-1]
        if os.path.isdir(temp): self.path=temp
        return
    def set_col(self,*Args):
        temp=list(self.column)
        _col = _SYS_FILE_CTRL_._cols
        for i in Args:
            temp[_col[i]] = True
        self.column = tuple(temp)
        return self.column
    def set_group(self,mode='DEFAULT'):
        if mode == 'DEFAULT':
            for n in self.data:
                if os.path.isdir(self.path + "\\" + n[0]): n[16] = "_FOLDER"
                elif os.path.isfile(self.path + "\\" + n[0]): n[16] = "_FILE"
                else: n[16] = "_UNKNOWN"
        if mode == 'FullName':
            alp_grp = misc.name_group((self.data[k][0] for k in range(len(self.data))),g_count=5,max_element=99)
            _grp_lst = []
            for g in alp_grp: _grp_lst.append(g[0]+g[1]);
            self.grp_lst  =tuple(_grp_lst)
            for i in range(len(self.data)):
                n=self.data[i];
                if not 'A' <= n[0][0].upper() <= 'Z': self.data[i][16] = '_Z'; continue;
                for g in alp_grp:
                    if (g[0] <= n[0][0].upper() <= g[1]): self.data[i][16] = str(g[0]+g[1])
        if mode == 'ExtOnly' or mode == 'EO_format':
            temp = set(self.data[k][2] for k in range(len(self.data)))
            print(temp)
        self.group = mode
    def reset_col(self):
        self.column=tuple((False for n in range(len(_SYS_FILE_CTRL_._cols))))
    def read(self):
        f_list = os.listdir(self.path)
        idx_dir = 0
        for i in f_list:
            filename = self.path + "\\" + i
            if   (os.path.isdir(filename) ): self.data.append(_SYS_FILE_CTRL_.getinfo(filename,self.column)); idx_dir +=1;
            elif (os.path.isfile(filename)): self.data.insert(idx_dir,_SYS_FILE_CTRL_.getinfo(filename,self.column));
            else: print(f"can't add item='{filename}' in List")
        return len(self.data)
    def cout(self,*Args):
        for n in self.data: print(*(n[_SYS_FILE_CTRL_._cols[a]] for a in Args),sep="\t");
    def sort(self,col):
        self.data = sorted(self.data, key=lambda x: x[col])
class _SYS_ROOT_DIR_:
    def __init___(self,*args):
        self._FS = []
        for cls in args: self._FS.append(cls());
    def read(self):
        pass
class _LNK_FAV_DIR_:
    _tag=[]
    def __init__(self):
        
        self.data=[]
        self.column = ()
        self.reset_col()
        self.set_col('FullName')
    def load_reg(REG): _tag = REG.load.data('_LNK_FAV_DIR_');
    def set_col(self,*Args):
        temp=list(self.column)
        _col = _SYS_FILE_CTRL_._cols
        for i in Args:
            temp[_col[i]] = True
        self.column = tuple(temp)
        return self.column
    def reset_col(self):
        self.column=tuple((False for n in range(len(_SYS_FILE_CTRL_._cols))))
    def read(self):
        for n in self.tag:
            self.data.append(_SYS_FILE_CTRL_.getinfo(n,self.column))
    def _select(self,idx):
        args ={}
        if self.data[idx][3] == "File Folder":
            t_module = "_SYS_FOLDER_"
            t =  self.data[idx][4]
            t = t if not t[-1:] == "\\" else t[0:-1]
            args['set_path'] = t + "\\" + self.data[idx][0]
        return (t_module,args)
    def cout(self,*Args):
        for n in self.data: print(*(n[_SYS_FILE_CTRL_._cols[a]] for a in Args),sep="\t");
class _SYS_RECYCLE_:
    pass
class _SYS_W_DRIVE_:
    _cols = {
        'Access'     : 0,'Caption'   : 1,'Compressed' : 2,'Description' : 3,'DeviceID' : 4,'DriveType' : 5,
        'FileSystem' : 6,'FreeSpace' : 7,'MediaType'  : 8,'Name'        : 9,'Size'     :10,'SystemName':11,
        'VolumeName' :12,'DT_format' :13,'FS_format'  :14,'Size_format' :15
        }
    drive_type=['Unknown','No Root Directory','Removable Disk'
        ,'Local Disk','Network Drive','Compact Disc' ]

    def __new__(cls, *args, **kwargs):
        if not importlib.util.find_spec('wmi'): return None;
        return super().__new__(cls)
    def __init__(self,*args):
        self._wmi = importlib.import_module('wmi')
        self.wmi_data=[]
        self.data = []
        self.column = ()
        self.reset_col()
        self.wmi_data = self._wmi.WMI().Win32_LogicalDisk();
    def set_col(self,*Args):
        temp=list(self.column)
        _col = self.__class__._cols
        for i in Args: temp[_col[i]] = True
        self.column = tuple(temp)
        return self.column
    def set_group(self,mode='DEFAULT'): pass;
    def reset_col(self): self.column=tuple((False for n in range(len(self.__class__._cols))))
    
    def read(self):
        #self.wmi_data = self._wmi.WMI().Win32_LogicalDisk();
        self.data = []
        col = self.column
        for k in self.wmi_data: 
            self.data.append(__class__.convert_wmi(k,self.column))
    def cout(self,*Args): print(*(n for n in self.data) ,sep="\t");
    def sort(self,col): pass;
    def getraw(self,*col):
        print(self.data)
        t_cidx = __class__._cols
        raw=[]
        for r in self.data:
            temp = []
            for c in col:
                print(c,t_cidx[c],end="\t")
                temp.append(r[t_cidx[c]])
            print(" ")
            raw.append(tuple(temp))
        return raw;
    @staticmethod
    def convert_wmi(input,_col):
        temp = list(_col)
        if _col[0]:  temp[0]  = input.Access
        if _col[1]:  temp[1]  = input.Caption
        if _col[2]:  temp[2]  = input.Compressed
        if _col[3]:  temp[3]  = input.Description
        if _col[4]:  temp[4]  = input.DeviceID
        if _col[5]:  temp[5]  = input.DriveType
        if _col[6]:  temp[6]  = input.FileSystem
        if _col[7]:  temp[7]  = input.FreeSpace
        if _col[8]:  temp[8]  = input.MediaType
        if _col[9]:  temp[9]  = input.Name
        if _col[10]: temp[10] = input.Size
        if _col[11]: temp[11] = input.SystemName
        if _col[12]: temp[12] = input.VolumeName
        if _col[13]: temp[13] = __class__.drive_type[int(input.DriveType)] if int(input.DriveType) in range (0,15) else "Unknown"
        if _col[14]: temp[14] = misc.data_size(input.FreeSpace if input.FreeSpace else 0)
        if _col[15]: temp[15] = misc.data_size(input.Size if input.Size else 0)
        return temp;

class misc:
    @staticmethod
    def Arg_Pharse(input,start =0,end=-1):
        output ={}
        param =""
        for i in range(start,len(input)):
            word = input[i] 
            if (word[0] == "-"):
                param = word[1:]
                output[param] = []
            else:
                if (param == ""): continue
                else: output[param].append(word)
        return output
    def data_size(n,_type='A',_format=False):
        n=int(n)
        if (not n): return 0
        if(_type == 'K'): v = (n/1024            if (not _format) else misc._data_size_trim(n/1024           ,f=_format), " KB");
        if(_type == 'M'): v = (n/1048576         if (not _format) else misc._data_size_trim(n/1048576        ,f=_format), " MB");
        if(_type == 'G'): v = (n/1073741824      if (not _format) else misc._data_size_trim(n/1073741824     ,f=_format), " GB");
        if(_type == 'T'): v = (n/1048576/1048576 if (not _format) else misc._data_size_trim(n/1048576/1048576,f=_format), " TB");
        if(_type == 'A'):
            #if (n < 1000): v =( _data_size_trim(n), " B")
            if (1 <= n < 1024000       ): v = (misc._data_size_trim(n/1024)      , " KB")
            elif (1000 <= n < 1048576000    ): v = (misc._data_size_trim(n/1048576)   , " MB")
            elif (1000 <= n < 1073741824000 ): v = (misc._data_size_trim(n/1073741824), " GB")
            else: v = (misc._data_size_trim(n/1048576/1048576), " TB");
        return str(v[0] if v[0] >= 1 else 1) + v[1]
    def _data_size_trim(n,d=3, f = False):
        temp = round(n)
        if   (temp > 1000): return temp if (not f) else f'{temp:,}' ;
        elif (1000 > temp > 99): return round(n) if (d<=3) else round(n,d-3);
        elif ( 100 > temp >  9): return round(n) if (d<=2) else round(n,d-2);
        elif (  10 > temp >= 0): return round(n) if (d<=1) else round(n,d-1);
    def name_group(lst,g_count=5,max_element=99):
        idx = [0 for n in range(26)]
        for n in lst:
            if ('A' <= n[0].upper() <= 'Z'): idx[ord(n[0].upper())-65] +=1
            else: continue;
        gsize = round(sum(idx)/g_count)
        grp=[]
        t=0
        i=0
        f='A'
        while i < 26:
            if (t >= gsize):
                grp.append((f,chr(i+65)))
                f = chr(i+65+1)
                t = 0
            t += idx[i]
            i +=1
        if not grp[-1][1] == 'Z':   grp[-1] = (grp[-1][0],'Z')
        return tuple(grp)
