import lib.debug as dg
#dg.cout("hello")
#dg.cout("hello",7858)
#dg.cout("hello",trace=True)
#dg.cout([7,"fefe"])
#dg.cout(["hello","fefe"],7858)
#dg.cout(["hello","fefe"],trace=True)
#dg.cout({1:"hello","ll":"jviueiue"})
#dg.cout({1:"hello","ll":"jviueiue"},7858)
dg.cout({1:"hello","ll":"jviueiue"},trace=True)

'''
import msvcrt
e_sKey = False
for i in range(1,10):
	live_input = msvcrt.getch()
	if (e_sKey):
		if(live_input.upper() == b'H'):
			print('up')
		if(live_input.upper() == b'P'):
			print('down')
		e_sKey = False
	else:
		if (live_input == b'\x00'):
			e_sKey = True

'''