import time
from ahk import AHK
ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\AutoHotkey.exe')
f = open("guinea-pig.ahk", "r")
if f.mode == "r":
	ahk_script = f.read()
print(ahk_script)
ahk.run_script(ahk_script, blocking=False)