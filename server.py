import socket
import sys
from _thread import *

try :
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    print ("socket created")
except Exception as e:
    print("Socket cannot be created : ", e)

server_ip = "127.0.0.1"
server_port = 4312

server.bind((server_ip, server_port))
# IP_address = str(sys.argv[1]) 
# Port = int(sys.argv[2])
# server.bind((IP_address, Port))
print ("socket port : ", server_port)

server.listen(10)

def serverThread(conn,addr):
    while True:
        message = conn.recv(2048)
        message=message.decode()
        print("details of client : ",message)


        msg_status = ""
        conn.send(msg_status.encode())




while True: 
	conn, addr = server.accept() 
			
	# list_of_clients.append(addr[1]) 
			
	print (addr[0] + " connected") 

	start_new_thread(serverThread,(conn,addr)) 

# conn.close() 
server.close() 

