import socket
import threading
import base64
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("Hello from thread: " + str(self.threadID))

        server.bind((socket.gethostname(), 5000))
        server.listen()
        conn,addr =server.accept()
        while True:
            data=conn.recv(16)
            print("Recieved data:")
            print(data.decode("utf-8"))
            if data:

                conn.send(data)
            else:
                break
#        message = "Hey\n".encode("utf-8")
 #       time.sleep(1)
  #      server.send(message)
        conn.detach()
        conn.close()

    def sendMsg(self, socket, msg):
        None


thread = myThread(1, "Thread 1")
thread.start()
time.sleep(1)
print("Hello wiord")
client = socket.socket()
client.connect((socket.gethostname(), 5000))
time.sleep(1)



client.send("hey".encode("utf-8"))
#data = client.recv(1024)
data=client.recv(16)
print("Client")
print(data.decode("utf-8"))
client.close()
#print(data.decode("utf-8"))
print("doen")
