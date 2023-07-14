import socket
import platform
import os


def info(ip, port):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except:
        return False
    else:
        return True

def clear():
    if platform.system() == "Windows":
        os.system("cls")

    if platform.system() == "Linux":
        os.system("clear")

ip = input("Enter IP: ")
clear()
print("Scanning " + ip, "for ports")


for port in range (1, 65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    if info(ip, port):
        print(ip, ":", port, "is open")
    else:
        print(ip, ":", port, "is closed")