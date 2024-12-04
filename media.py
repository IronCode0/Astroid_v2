
import os
import cmd      # https://docs.python.org/3/library/cmd.html
from lib.datalib import quick
from lib.FShandle import _SYS_FILE_CTRL_ as fl
from lib.FShandle import _SYS_FOLDER_ as fr
from lib.FShandle import misc
wdir="F:\\Ani\\_Download\\system"

class str:
    @staticmethod
    def phraseRX(text,**kwargs):pass
    def split(text,der=" "): pass

class Shell(cmd.Cmd):
    intro = 'Welcome to the IronCode0 shell.   Type help or ? to list commands.\n'
    prompt = '(root) '
    file = None
    dir=""
    def set_dir(self,path=None):
        if not path or not os.path.exists(path): return
        self.dir=path
        os.chdir(path)
        self.fs.set_path(path)
        self.prompt=path+">"
        return self
    def configure(self,*args):
        self.fs=fr(fileinfo=fl)
        self.set_dir(args[0])
        return self
    def do_dir(self,args):
        self.fs.set_col('FullName','NameNoExt', 'ExtOnly','DM_format','ByteSize' , 'BS_format')
        self.fs.read()
        lst=self.fs.get_data('DM_format','ByteSize','FullName')
        tsize=sum([i[1] for i in lst])
        print(*["\t".join(i) for i in quick.pad2d(lst,align=('LRL'))],sep="\n")
        print(f'\tFile: {len(lst)}\n\tSize: {misc.data_size(tsize,'A',True)}')
    def do_exit(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print('Thank you for using IronCode0 shell')
        self.close()
        return True

    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    Shell().configure(wdir).cmdloop()
