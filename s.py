import socket
import pickle
import mysql.connector as my

con=my.connect(host='192.168.43.29',port='3306',user='vip',password='vip12345', database='chat')

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cursor=con.cursor()
cursor.execute('SELECT * FROM shop')

host = socket.gethostname()
port=1235
s.bind((host,port))

s.listen()
socketclient,address = s.accept()
for i in cursor:
	socketclient.send(i)
print("GOT Connected to",address)
con=True
while con:
	msg=socketclient.recv(1024)
	msg=msg.decode("utf-8")
	if msg == 'quit':
		con=False
		s.close()
		print('bye.......')
	print(msg)
