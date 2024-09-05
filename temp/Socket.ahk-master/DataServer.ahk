#NoEnv
SetBatchLines, -1
CoordMode, Mouse, Screen

#Include ..\Socket.ahk
Server := new SocketTCP()
Server.OnAccept := Func("OnAccept")
Server.Bind(["0.0.0.0", 1337])
Server.Listen()

MsgBox, Serving on port 1337`nClose to ExitApp
ExitApp



OnAccept(Server) {
	global Template
	static Counter := 0
	
	Sock := Server.Accept()
	Request := StrSplit(Sock.RecvLine(), " ")
	
	; You need to empty the Recv buffer before responding to the HTTP request whether you use that data or not
	while Line := Sock.RecvLine()
		Table .= Format("<tr><td>{}</td><td>{}</td></tr>", StrSplit(Line, ": ")*)
	
	if (Request[1] != "GET")
	{
		Sock.SendText("HTTP/1.0 501 Not Implemented`r`n`r`n")
		Sock.Disconnect()
		return
	}
	
	if (Request[2] == "/")
		Sock.SendText(Format(Template, Table, ++Counter))
	else if (Request[2] == "/mouse")
	{
		MouseGetPos, x, y
		Sock.SendText("HTTP/1.0 200 OK`r`n`r`n" x "," y)
	}
	else if (Request[2] == "/favicon.ico")
		Sock.SendText("HTTP/1.0 301 Moved Permanently`r`nLocation: https://autohotkey.com/favicon.ico`r`n")
	else
		Sock.SendText("HTTP/1.0 404 Not Found`r`n`r`nHTTP/1.0 404 Not Found")
	Sock.Disconnect()
}
