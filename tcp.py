from socket import *
import os
import struct
import time

class communicator():
    class SocketInfo():
        HOST=SERVER_NAME
        PORT=SERVER_PORT
        BUFSIZE=100
        ADDR=(HOST, PORT)
    
    def __init__(self):
        self.csock = socket(AF_INET, SOCK_STREAM)

        while self.csock.connect_ex(self.SocketInfo.ADDR):
            print(f"tcp connect error")
            time.sleep(1)
        
        print("conenct is success")

    def __del__(self):
        self.csock.close()   

    def send_int(self, input: int):
        input_byte = struct.pack('<i', input)
        self.csock.send(input_byte)

    def recv_int(self):
        recv_bytes = self.csock.recv(4)
        recv_int = struct.unpack('<i', recv_bytes)
        return recv_int[0]

    def send_float(self, input):
        input_byte = struct.pack('<f', input)
        self.csock.send(input_byte)
    
    def recv_float(self):
        recv_bytes = self.csock.recv(4)
        recv_float = struct.unpack('<f', recv_bytes)
        return recv_float[0]

if __name__ == '__main__':
    connect = communicator()

    pid = os.getpid()
    connect.send_int(pid)
    print(f"pid is {pid}")

    ret = connect.recv_int()
    print(ret)

    connect.send_float(3.14159265358979323846)

    