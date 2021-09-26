import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port=1235

s.connect((host,port))
socketclient,address = s.accept()
msg=socketclient.recv(1024)
msg=msg
print(msg)

con=True
while con:
	msg=input('Enter Msg: ')
	s.send(msg.encode("utf-8"))
	if msg == 'quit':
		con=False
		s.close()
		