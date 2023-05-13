#biblioteca para gerar o servidor
import socket
#portas e o ip do host
host = '127.0.0.1'
port = 5000

#definição de qual serve vai ser usado
servetc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#passando por parametros a origem do servidor
origem = (host, port)

#resevando e ouvindo o servidor
servetc.bind(origem)
servetc.listen()
#abrindo conecção com cliente
while True:
    con, client = servetc.accept()
    print("Cliente conectado", client)
    while True:
        msg = con.recv(1024)
        print(client, msg)
        