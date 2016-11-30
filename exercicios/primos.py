"""
Disciplina:	Programação Orientada a Objetos
Professor:	Orlewilson B. Maia
Turma:		RCN04S1

Autor:		Orlewilson B. Maia
Data:		29/11/2016
Descrição:	Classe para representar dados de um 
		    número primo

"""

class Primo():

	# atributos
	__numero = 0
		
	# construtor
	def __init__(self, 
				 numero = 0):
		self.setNumero(numero)

	def setNumero(self, numero):
		self.__numero = numero

	def getNumero(self):
		return self.__numero

	def ePrimo(self):
		if self.getNumero() < 2:
			return False
		else:
			for n in range(2, self.getNumero()):
				if self.getNumero() % n == 0:
					return False
			return True

# Exemplo objeto
primo = Primo(131)
print(primo.ePrimo())