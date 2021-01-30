import socket

class Sever():
    def __init__(self, id, port):    
        self.queue = []
        self.games = []
        self.ip = "192.168.1.15"
        self.port = 8888
        self.addr = (ip, port)

    def player(conn, player):
        

    def handle_queue():
        pass

    def connect():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(self.addr)
        s.listen()
        self.handle_queue()