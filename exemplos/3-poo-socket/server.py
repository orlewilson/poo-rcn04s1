"""
Disciplina:	Programação Orientada a Objetos
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		10/11/2016
Descrição:	Exemplo de soquete (socket) servidor 
			em Python utilizando POO.

Fonte:		https://shakeelosmani.wordpress.com/
			2015/04/13/python-3-socket-programming-
			example/

"""
# importa a biblioteca para trabalhar com soquete
import socket

# importar classes
from geladeira import Geladeira

# criar objetos
samsung = Geladeira()

samsung.setTemperatura(23.2)
samsung.ligar()

# configurações do servidor

host = '127.0.0.1' 		# IP
port = 5005				# Porta
 
# Criando um objeto do tipo soquete (socket)
mySocket = socket.socket()

# Informa a o IP e a porta que ficará escutando
mySocket.bind((host,port))

# Adiciona um listening para escutar as solicitações
mySocket.listen(1)

# Quando chegar uma solicitação, obtém a comunicação e o endereço do cliente
conn, addr = mySocket.accept()

print ("IP do cliente conectado: " + str(addr))

while True:
	data = conn.recv(1024).decode()
	if not data:
		break
	
	print ("Mensagem recebida do cliente: " + str(data))

	if (str(data).upper().find("STATUSGELADEIRA")>=0):
		data = str(samsung.verificarStatus())
             
	#data = str(data).upper()
	print ("Mensagem enviada para o cliente: " + str(data))
	conn.send(data.encode())
             
conn.close()