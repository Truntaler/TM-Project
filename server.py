import socket
import pickle

class Sever():
    def __init__(self, id, port):    
        self.queue = []
        self.games = []
        self.addr = (ip, port)

    def player(self, conn, player):
        msg = {}

    def handle_queue(self, player):
        pass

    def handle_games(self, game):
        pass

    def connect(self):
        ip = "192.168.1.15" # meine ip bitte nicht ddosen
        port = 8888

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind(self.addr)
        except socket.error as error:
            print(error)
        
        s.listen()
        
        while True: 
            conn, addr = s.accept()
            self.handle_game()