import socket, Queue, signal
import sys
from thread import *
global ALIVE
ALIVE = True

def strip_join_message(join_string):
	rough_details = join_string.split("\n")
	details = rough_details[0:3]
	for i in details:
		client_details[i] = details[i].split(" ").[1]
	return client_details

def create_join_message():

def room_exists(room_name, chatrooms):
	exists = False
	for room in enumerate(chatrooms):
		if chatrooms[room][0]==room_name
			return room
	return -1

def clientthread(quu, chatrooms):
	global ALIVE
	while ALIVE:
		blocked = True
		while blocked:
			blocked = False
			try:
				connectionTuple = quu.get()
			except Queue.Empty as emp:
				blocked = True

		conn = connectionTuple[0]
		addr = connectionTuple[1]
		print 'Connected to ' + addr[0] + ':' + str(addr[1])

		while True:
			data = conn.recv(1024)
			if data.startswith("HELO ")
				start = data[5:]
				reply = data+"\nIP:"+str(addr[0])+"\nPort:"+str(PORT)+"\nStudentID:11816252"
			elif data=="KILL_THREAD\n":
				break
			elif data=="KILL_SERVICE\n":
				reply = "panic"
				ALIVE = False
				break
			elif data.startswith("JOIN_CHATROOM"):
				details = strip_join_message(data)
				room_index = room_exists(details[0])
				if room_index == -1
					#add chat room
					chatrooms.append([[details[0],'localhost', PORT]])
					reply = create_join_message([details[0],'localhost',PORT])
				else:

			elif data is None:
				break
			else:
				reply = data.upper()
			conn.send(reply)
		conn.close()

def main():
	HOST = ''
	PORT = int(sys.argv[1]) #paramterised port number
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	quu = Queue.Queue()
	chatrooms = [];

	try:
		s.bind((HOST, PORT))
	except socket.error as msg:
		print 'Bind failed'
		sys.exit(

	s.listen(5)
	print 'Socket now listening'

	for x in range(0, 10):
		start_new_thread(clientthread, (quu, chatrooms))
	while ALIVE:
		conn, addr = s.accept()
		quu.put((conn,addr))
	s.close()

main()
