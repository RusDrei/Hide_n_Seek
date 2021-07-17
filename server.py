import socket
from _thread import *
import sys

server = ''         # local address         to get go to command prompt and type 'ipconfig'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as error:
    str(error)


s.listen(2)     # 2 players
print('connecting')

def threaded_client(conn):
    while True:
        try:
            data = conn.recv(2048)
            reply = data.encode('utf-8')

            if not data:
                print('Disconnected')
                break
            else:
                print('Recieved: ', reply)
                print('Sending: ', reply)
            conn.sendall(str.encode(reply))

        except:
            break


while True:
    connection, addr = s.accept()
    print('Connected to: ', addr)

    start_new_thread(threaded_client, (connection,))