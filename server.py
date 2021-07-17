import socket
from _thread import *
import sys


def threaded_client(conn):
    conn.send(str.encode('Connected'))

    while True:
        try:
            data = conn.recv(1024)
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


server = ''         # local address         to get go to command prompt and type 'ipconfig'
port = 5000

s = socket.socket()

try:
    s.bind((server, port))
except socket.error as error:
    str(error)

s.listen(5)     # 5 players
print('Waiting for connection')

while True:
    print('*')
    connection, addr = s.accept()
    print('Connected to: ', addr)

    start_new_thread(threaded_client, (connection,))

