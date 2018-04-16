import threading
import socket
import time


class client(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        print("Hello from "+str(self.name))
        time.sleep(1)
        server=socket.socket()
        server.connect((socket.gethostname(),3000))
        port=server.recv(1024)
        print(port)