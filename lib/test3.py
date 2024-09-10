class REG:
    def __init__(self):
        self.val = 0
        self.main = self.Node(0)
    def write(self,addr,value):
        if addr == "": return 0
        loc = self.main
        for n in addr.split("/"):
            if n not in loc.children: loc.add(n,self.Node())
            loc = loc.children[n]
        loc.val = value
    def read(self,addr):
        if addr == "": return 0
        loc = self.main
        for n in addr.split("/"):
            if n not in loc.children: return 0
            loc = loc.children[n]
        return loc.val
    def set_raw(self,raw,root=None):
        if not root: root = self.main;
        p=0
        l= len(raw)
        brc = 0
        while p < l:
            if raw[p] == "<":
                brc +=1
                s1=p
                while not raw[s1] == "=": s1 +=1
                key = raw[p+1:s1]
                s2 = s1
                while s2 < l:
                    s2 +=1
                    if raw[s2] == "<": break #new
                    if raw[s2] == ">": break;
                val = raw[s1+1:s2]
                #print(key,val)
                root.children[key] = self.Node(val)
                #print( root.children[key])
                if raw[s2] == "<": 
                    end = 0
                    t=l-1
                    while end != brc:
                        if raw[t] == ">": end +=1;
                    p = self.set_raw(raw[s2:end],root.children[key]);
            p += 1
            if raw[p] == ">": brc-= 1;
            if brc == 0: break;
        return p
    def get_raw(self):
        text= __class__._rec_phrase(self.main)
        return text
    def _rec_phrase(addr):
        #print(addr.children)
        text = ""
        if not addr.children: return text
        for e in addr.children:
            print(e)
            child = addr.children[e]
            text +="<"+ e + "=" + str(child.val) + __class__._rec_phrase(child) + ">"
        return text


    class Node:
        def __init__(self,value = 0) -> None:
            self.val = value
            self.children = {}
        def add(self,param,child):
            self.children[param] = child
            return child
        def get(self,param):
            return self.children[param]

t = REG()
'''
t.write("LV/color",7)
t.write("LV/size/h",400)
t.write("LV/back",74)
t.write("RV/back",44)
t.write("LV/back/egege/gegege",77)
t.write("TS/back/egege/gegege",74)
t.write("TS/back/egege",74)
t.write("LV/for",5)
t.write("LV/size/w",600)
t.write("LV/color/force",999)

print(t.read("LV/size/h"))
print(t.save_file())
'''
raw="<LV=0<color=7<force=999>><size=0<h=400><w=600>><back=74<egege=0<gegege=77>>><for=5>><RV=0<back=44>><TS=0<back=0<egege=74<gegege=74>>>>"

#t.set_raw(raw)



_dict = {
            '001'  : 'File',
            '111'  : '111 File',
            '7z'   : '7-Zip archive',
            'accdb': 'Microsoft Office Access 2007 Database',
            'ace'  : 'File',
            'acl'  : 'AutoCorrect List File',
            'ahk'  : 'AutoHotkey Script',
            'amr'  : 'media file',
            'amv'  : 'media file',
            'apk'  : 'Androide Application',
            'arj'  : 'File',
            'avi'  : 'File',
            'bat'  : 'Windows Batch File',
            'bmp'  : 'Bitmap image',
            'bz2'  : 'File',
            'bzip2': 'File',
            'cab'  : 'CAB archive',
            'chk'  : 'Recovered File Fragments',
            'chm'  : 'Compiled HTML Help file',
            'config' : 'XML Configuration File',
            'contact': 'Contact file',
            'cpio' : 'File',
            'cpp'  : 'C++ Source',
            'crl'  : 'Certificate Revocation List',
            'csf'  : 'CSF File',
            'css'  : 'Cascading Style Sheet Document',
            'csv'  : 'Microsoft Office Excel Comma Separated Values File',
            'db'   : 'Data Base File',
            'deb'  : 'File',
            'divx' : 'media file',
            'dll'  : 'Application extensio',
            'dmg'  : 'File',
            'dmp'  : 'Crash Dump File',
            'doc'  : 'Microsoft Office Word 97 - 2003 Document',
            'docm' : 'Microsoft Office Word Macro-Enabled Document',
            'docx' : 'Microsoft Office Word Document',
            'dot'  : 'Microsoft Office Word 97 - 2003 Template',
            'dotm' : 'Microsoft Office Word Macro-Enabled Template',
            'dotx' : 'Microsoft Office Word Template',
            'dsn'  : 'Data Source Name',
            'DTD'  : 'XML Document Type Definition',
            'emf'  : 'EMF File',
            'exe'  : 'Application',
            'fat'  : 'File',
            'gif'  : 'GIF image',
            'gz'   : 'File',
            'gzip' : 'File',
            'h'    : 'C/C++ Header',
            'hfs'  : 'File',
            'HLP'  : 'Help file',
            'htm'  : 'Firefox HTML Document',
            'html' : 'File',
            'icc'  : 'ICC Profile',
            'icl'  : 'Unknown',
            'ico'  : 'Icon',
            'idoc' : 'File',
            'ini'  : 'Configuration settings',
            'iso'  : 'File',
            'jar'  : 'File',
            'jpeg' : 'Jpeg image',
            'jpg'  : 'JPEG image',
            'js'   : 'JScript Script File',
            'lex'  : 'Dictionary File',
            'lha'  : 'File',
            'lib'  : 'Object File Library',
            'lnk'  : 'Shortcut',
            'lst'  : 'MASM Listing',
            'lzh'  : 'File',
            'lzma' : 'File',
            'm4v'  : 'MP4 Video',
            'mdw'  : 'Microsoft Office Access Workgroup Information',
            'mht'  : 'MHTML Document',
            'mp3'  : 'MPEG Layer 3 Audio File',
            'mp4'  : 'MP4 Video',
            'mpg'  : 'Movie Clip',
            'msi'  : 'Windows Installer Package',
            'ntfs' : 'File',
            'odt'  : 'OpenDocument Text',
            'one'  : 'Microsoft Office OneNote Section',
            'opus' : 'media file',
            'pbk'  : 'Dial-Up Phonebook',
            'pdb'  : 'Program Debug Database',
            'pdf'  : 'PDF Document',
            'pmc'  : 'Macro Creator File',
            'pmd'  : 'File',
            'png'  : 'PNG image',
            'ppp'  : 'Photo Pad Project',
            'ppt'  : 'File',
            'pptx' : 'File',
            'psd'  : 'Adobe Photoshop Image',
            'pub'  : 'Microsoft Office Publisher Document',
            'rar'  : 'WinRAR archive',
            'rdp'  : 'Remote Desktop Connection',
            'reg'  : 'Registration Entries',
            'rm'   : 'media file',
            'rpm'  : 'File',
            'rtf'  : 'Rich Text Document',
            'slk'  : 'Microsoft Office Excel SLK Data Import Format',
            'sln'  : 'Microsoft Visual Studio Solution',
            'sst'  : 'Microsoft Serialized Certificate Store',
            'suo'  : 'Visual Studio Solution User Options',
            'svg'  : 'SVG Document',
            'swf'  : 'Shockwave Flash',
            'swm'  : 'File',
            'tar'  : 'File',
            'taz'  : 'File',
            'tbz'  : 'File',
            'tbz2' : 'File',
            'tgz'  : 'File',
            'theme': 'Windows Theme File',
            'thmx' : 'Microsoft Office Theme',
            'tpz'  : 'File',
            'ttf'  : 'TrueType font file',
            'txt'  : 'Text Document',
            'txz'  : 'File',
            'url'  : 'Internet Shortcut',
            'uue'  : 'File',
            'vbs'  : 'VBScript Script File',
            'vhd'  : 'File',
            'webm' : 'WebM Video',
            'webp' : 'Chrome HTML Document',
            'wim'  : 'File',
            'wmv'  : 'Windows Media Audio/Video file',
            'wpl'  : 'Windows Media playlist',
            'wtv'  : 'Windows Recorded TV Show',
            'xar'  : 'File',
            'xla'  : 'Microsoft Office Excel Add-In',
            'xls'  : 'Microsoft Office Excel 97-2003 Worksheet',
            'xlsb' : 'Microsoft Office Excel Binary Worksheet',
            'xlsm' : 'Microsoft Office Excel Macro-Enabled Worksheet',
            'xlsx' : 'Microsoft Office Excel Worksheet',
            'xltm' : 'Microsoft Office Excel Macro-Enabled Template',
            'xltx' : 'Microsoft Office Excel Template',
            'xml'  : 'XML Document',
            'xps'  : 'XPS Document',
            'xsl'  : 'XSLT Stylesheet',
            'xsn'  : 'Microsoft Office InfoPath Form Template',
            'xspf' : 'Winamp playlist file',
            'xss'  : 'Visual Studio Dataset Internal Info File',
            'xvid' : 'XVID File',
            'xz'   : 'File',
            'z'    : 'File',
            'zip'  : 'ZIP archive'
            }
            

from sys import getsizeof as gs
gs(_dict)