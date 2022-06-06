import os

os.system("netsh wlan show profiles Smartone_Direction key=clear > output.txt")
with open("output.txt", "r") as fichier:
    fichier = fichier.read()
    print(fichier)