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
print ("socket port : ", server_port)

server.listen(10)


def parseInput(data):


def serverThread(conn,addr):
    while True:
        message = conn.recv(2048)
        message=message.decode()
        print("details of client : ",message)
        bin_data, matrix = parseInput(message)
        data_matrix = np.array(data_matrix)
        appended_data = bin_data + '0'*(len(key)-1)
        remainder = get_remainder(appended_data, divisor)

        decoded_data = np.dot(cipher_matrix, data_matrix.T)

        msg_status = ""
        conn.send(msg_status.encode())




while True: 
	conn, addr = server.accept() 
			
	# list_of_clients.append(addr[1]) 
			
	print (addr[0] + " connected") 

	start_new_thread(serverThread,(conn,addr)) 

# conn.close() 
server.close() 

