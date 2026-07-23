import socket
import time

# HOST = "192.168.4.31"
# PORT = 1313

class Client:
    def __init__(self, ip, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip, port))
        print("Connected!")

    def stop(self):
        self.client.close()


client = Client("192.168.4.33", 1313)
time.sleep(1)
client.stop()