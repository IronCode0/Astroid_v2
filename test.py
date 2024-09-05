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

