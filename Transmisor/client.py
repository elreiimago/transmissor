import socket
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(("192.168.1.2", 8080))
    print("Connected")

except:
    print("Error")
