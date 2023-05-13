#biblioteca para gerar o servidor
import socket
#portas e o ip do host
host = '127.0.0.1'
port = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

destino = (host,port)

tcp.connect(destino)
while True:
    msg = input()
    tcp.send(str.encode(msg))