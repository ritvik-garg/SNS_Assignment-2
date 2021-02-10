import socket
import sys

try :
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("socket created")
except Exception as e:
    print("Socket cannot be created : ", e)

server_ip = "127.0.0.1"
server_port = 4312

server.connect((server_ip, server_port))

divisor = 1001

ascii_a = ord('a')

def convertData(data):
    res = ""
    plaintext_matrix = []
    for char in data:
        if char==' ':
            res+= format(27, 'b')
            plaintext_matrix.append(27)
        else:
            ascii_val = ord(char)
            new_ascii = ascii_val-ascii_a+1
            plaintext_matrix.append(new_ascii)
            res+= format(new_ascii, 'b')

    size_of_matrix = len(plaintext_matrix)

    while(len(plaintext_matrix)%3 != 0):
        plaintext_matrix.append(27)

    return res, plaintext_matrix


while True:
    input_msg = sys.stdin.readline()
    server.send(message.encode())
    from_server = server.recv(1024)
    print ("from server : ", from_server)

server.close()