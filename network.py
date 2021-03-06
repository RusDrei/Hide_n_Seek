import socket

class Network:
    def __init__(self):
        self.client = socket.socket()
        self.server = '95.73.147.89'
        self.port = 5000
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        print(self.pos)

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print('Network error send method: ', e)


n = Network()
print(n.send('hi'))
