
import os
class file:
    def __init__(self,path=""):
        if not os.path.exists(path): __class__.create_file(path)
        self.fullpath=path
    def create_file(path=""):
        head,tail = os.path.split(path)
        try:
            os.makedirs(head)
            print(f"Nested directories '{head}' created successfully.")
        except FileExistsError:
            print(f"One or more directories in '{head}' already exist.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{head}'.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return path
        
    def read(self,var=""):
        f = open(self.fullpath,"r")
        if (f): raw = f.readlines()
        else: raw = ""
        f.close()
        if type(var) is list:
            var[0] +=raw
            return self
        return raw
    def write(self,data="",newpath=""):
        path=self.fullpath
        if (newpath !="" and newpath != self.fullpath):
            path = __class__.create_file(newpath)
        print(path)
        f = open(path,'w')
        if type(data) is list: f.writelines(data)
        else: f.write(data)
        f.close()
        return self
        
            

