#coding=utf-8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = input("LHOST: ")
port = int(input("LPORT: "))
s.bind((ip_address, port))
s.listen(5)

while True:
    try:
        connexion, address = s.accept()
    except:
        print("Client disconnected, you must try again")
    else:
        print("Client connection on {}".format(ip_address))
        message = connexion.recv(1024)
        print(message.decode())
        break
    finally:
        print("Le scénario est terminé")
