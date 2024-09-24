#from reg import REG as RE
class reg:
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
    def load_file():
        pass
    def export_raw(self,addr="/",root=""):
        if root == "": root =self.main;
        if addr[0]=='/': addr = addr[1:]
        text = addr + "=" + str(root.val) + "\n"
        for c in root.children:
            text +=__class__.export_raw(self,addr+"/"+c,root.children[c])
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
    @staticmethod
    
    class load:
        def FileType(src=""):
            _dict = {
            '001' : 'File',
            '111' : '111 File',
            '7z' : '7-Zip archive',
            'accdb' : 'Microsoft Office Access 2007 Database',
            'ace' : 'File',
            'acl' : 'AutoCorrect List File',
            'ahk' : 'AutoHotkey Script',
            'amr' : 'media file',
            'amv' : 'media file',
            'apk' : 'Androide Application',
            'arj' : 'File',
            'avi' : 'File',
            'bat' : 'Windows Batch File',
            'bmp' : 'Bitmap image',
            'bz2' : 'File',
            'bzip2' : 'File',
            'cab' : 'CAB archive',
            'chk' : 'Recovered File Fragments',
            'chm' : 'Compiled HTML Help file',
            'config' : 'XML Configuration File',
            'contact' : 'Contact file',
            'cpio' : 'File',
            'cpp' : 'C++ Source',
            'crl' : 'Certificate Revocation List',
            'csf' : 'CSF File',
            'css' : 'Cascading Style Sheet Document',
            'csv' : 'Microsoft Office Excel Comma Separated Values File',
            'db' : 'Data Base File',
            'deb' : 'File',
            'DeskLink' : 'Desktop Shortcut',
            'divx' : 'media file',
            'dll' : 'Application extensio',
            'dmg' : 'File',
            'dmp' : 'Crash Dump File',
            'doc' : 'Microsoft Office Word 97 - 2003 Document',
            'docm' : 'Microsoft Office Word Macro-Enabled Document',
            'docx' : 'Microsoft Office Word Document',
            'dot' : 'Microsoft Office Word 97 - 2003 Template',
            'dotm' : 'Microsoft Office Word Macro-Enabled Template',
            'dotx' : 'Microsoft Office Word Template',
            'dsn' : 'Data Source Name',
            'DTD' : 'XML Document Type Definition',
            'emf' : 'EMF File',
            'exe' : 'Application',
            'fat' : 'File',
            'filters' : 'VC++ Project Filters File',
            'gif' : 'GIF image',
            'gz' : 'File',
            'gzip' : 'File',
            'h' : 'C/C++ Header',
            'hfs' : 'File',
            'HLP' : 'Help file',
            'htm' : 'Firefox HTML Document',
            'html' : 'File',
            'icc' : 'ICC Profile',
            'icl' : 'Unknown',
            'ico' : 'Icon',
            'idoc' : 'File',
            'ini' : 'Configuration settings',
            'iso' : 'File',
            'jar' : 'File',
            'jpeg' : 'Jpeg image',
            'jpg' : 'JPEG image',
            'js' : 'JScript Script File',
            'lex' : 'Dictionary File',
            'lha' : 'File',
            'lib' : 'Object File Library',
            'lnk' : 'Shortcut',
            'lst' : 'MASM Listing',
            'lzh' : 'File',
            'lzma' : 'File',
            'm4v' : 'MP4 Video',
            'MAPIMail' : 'Mail Service',
            'mdw' : 'Microsoft Office Access Workgroup Information',
            'mht' : 'MHTML Document',
            'mp3' : 'MPEG Layer 3 Audio File',
            'mp4' : 'MP4 Video',
            'mpg' : 'Movie Clip',
            'msi' : 'Windows Installer Package',
            'mydocs' : 'MyDocs Drop Target',
            'ntfs' : 'File',
            'odt' : 'OpenDocument Text',
            'one' : 'Microsoft Office OneNote Section',
            'onepkg' : 'Microsoft Office OneNote Single File Package',
            'onetoc2' : 'Unknown',
            'opus' : 'media file',
            'pbk' : 'Dial-Up Phonebook',
            'pdb' : 'Program Debug Database',
            'pdf' : 'PDF Document',
            'pmc' : 'Macro Creator File',
            'pmd' : 'File',
            'png' : 'PNG image',
            'ppp' : 'Photo Pad Project',
            'ppt' : 'File',
            'pptx' : 'File',
            'psd' : 'Adobe Photoshop Image',
            'pub' : 'Microsoft Office Publisher Document',
            'rar' : 'WinRAR archive',
            'rdp' : 'Remote Desktop Connection',
            'reg' : 'Registration Entries',
            'ResmonCfg' : 'Resource Monitor Configuration',
            'rm' : 'media file',
            'rpm' : 'File',
            'rtf' : 'Rich Text Document',
            'search-ms' : 'Saved Search',
            'slk' : 'Microsoft Office Excel SLK Data Import Format',
            'sln' : 'Microsoft Visual Studio Solution',
            'squashfs' : 'File',
            'sst' : 'Microsoft Serialized Certificate Store',
            'suo' : 'Visual Studio Solution User Options',
            'svg' : 'SVG Document',
            'swf' : 'Shockwave Flash',
            'swm' : 'File',
            'tar' : 'File',
            'taz' : 'File',
            'tbz' : 'File',
            'tbz2' : 'File',
            'tgz' : 'File',
            'theme' : 'Windows Theme File',
            'thmx' : 'Microsoft Office Theme',
            'tpz' : 'File',
            'ttf' : 'TrueType font file',
            'txt' : 'Text Document',
            'txz' : 'File',
            'url' : 'Internet Shortcut',
            'uue' : 'File',
            'vbs' : 'VBScript Script File',
            'vcxproj' : 'VC++ Project',
            'vhd' : 'File',
            'vssettings' : 'Visual Studio Settings File',
            'webm' : 'WebM Video',
            'webp' : 'Chrome HTML Document',
            'wim' : 'File',
            'wmv' : 'Windows Media Audio/Video file',
            'wpl' : 'Windows Media playlist',
            'wtv' : 'Windows Recorded TV Show',
            'xar' : 'File',
            'xla' : 'Microsoft Office Excel Add-In',
            'xls' : 'Microsoft Office Excel 97-2003 Worksheet',
            'xlsb' : 'Microsoft Office Excel Binary Worksheet',
            'xlsm' : 'Microsoft Office Excel Macro-Enabled Worksheet',
            'xlsx' : 'Microsoft Office Excel Worksheet',
            'xltm' : 'Microsoft Office Excel Macro-Enabled Template',
            'xltx' : 'Microsoft Office Excel Template',
            'xml' : 'XML Document',
            'xps' : 'XPS Document',
            'xsl' : 'XSLT Stylesheet',
            'xsn' : 'Microsoft Office InfoPath Form Template',
            'xspf' : 'Winamp playlist file',
            'xss' : 'Visual Studio Dataset Internal Info File',
            'xvid' : 'XVID File',
            'xz' : 'File',
            'z' : 'File',
            'ZFSendToTarget' : 'Compressed (zipped Folder SendTo Target)',
            'zip' : 'ZIP archive'
            }
            return _dict
        def data(src=""):
            global reg_LV
            if (src == "_LNK_FAV_DIR_"):return ("F:\\Software","F:\\Downloads","C:\\Boot\\sm_da")
            if (src == "LV"): return reg_LV

reg_LV={
    '_SYS_W_DRIVE_': {
        'column_read': (
            'Caption'  ,'DriveType','DT_format'  ,'FileSystem','FreeSpace',
            'FS_format','Size'     ,'Size_format','VolumeName'
        ),
        'column_cout': (
            ('Caption',100),
            ('DT_format',100),
            ('FileSystem',100),
            ('FS_format',100),
            ('Size', 100),
            ('Size_format',100),
            ('VolumeName',100)
        )
    },
    '_SYS_FOLDER_': {
        'column_read': (
            'FullName'    ,'NameNoExt','ExtOnly'    ,'EO_format','FileAttribute',
            'DateModified','DM_format','DateCreated','DC_format','DateAccessed' ,
            'DA_format'   , 'ByteSize','BS_format'    
        ),
        'column_cout': (
            ('NameNoExt',100),
            ('EO_format',100),
            ('DM_format',100),
            ('DC_format',100),
            ('DA_format',100),
            ('BS_format',100)
        )
    }
    }