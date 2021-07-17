import socket
from _thread import *
import sys

server = '192.168.0.162'         # local address         to get go to command prompt and type 'ipconfig'
port = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as error:
    str(error)


s.listen(2)     # 2 players
print('Waiting for connection')

def threaded_client(conn):
    conn.send(str.encode('Connected'))

    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')

            if not data:
                print('Disconnected')
                break
            else:
                print('Received: ', reply)
                print('Sending: ', reply)

            conn.sendall(str.encode(reply))

        except:
            break
    print('lost connection')
    conn.close()


while True:
    connection, addr = s.accept()
    print('Connected to: ', addr)

    start_new_thread(threaded_client, (connection,))

