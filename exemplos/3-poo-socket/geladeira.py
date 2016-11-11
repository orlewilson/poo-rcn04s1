"""
Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		10/11/2016

Autor:		Orlewilson B. Maia
Descrição:	Classe para representar uma geladeira

"""

class Geladeira():

	#atributos
	__cor = ""
	__tamanho = ""
	__modelo =  ""
	__status = True
	__consumo = 0.0
	__temperatura = 0.0

	#construtor
	def __init__(self, cor = "", tamanho = "",
		modelo = "", status = True, consumo = 0.0,
		temperatura = 0.0):

		self.__cor = cor
		self.__tamanho = tamanho
		self.__modelo = modelo
		self.__status = status
		self.__consumo = consumo
		self.__temperatura = temperatura

	# métodos para acesso aos métodos
	def setTemperatura(self, temperatura):
		self.__temperatura = temperatura

	def getTemperatura(self):
		return self.__temperatura

	# outros métodos
	def verificarTemperatura(self):
		return self.getTemperatura()

	def ligar(self):
		self.__status = True
		#self.setStatus(True)

	def desligar(self):
		self.__status = False
		#self.setStatus(False)

	def verificarStatus(self):
		return self.__status
		