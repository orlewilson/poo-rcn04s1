"""
Disciplina:	Programação Orientada a Objetos
Professor:	Orlewilson B. Maia
Turma:		RCN04S1

Autor:		Orlewilson B. Maia
Data:		21/09/2016
Descrição:	Classe para representar dados de um 
		    professor

"""

class Professor():

	# atributos
	__nome = ""
	__salario = 0.0
	__cpf = ""
	__endereco = ""
	__idade = 0

	# construtor
	def __init__(self, 
				 nome = "", 
				 salario = 0.0,
				 cpf = "",
				 endereco = "",
				 idade  = 0):
		self.setNome(nome)
		self.setSalario(salario)
		self.setCpf(cpf)
		self.setEndereco(endereco)
		self.setIdade(idade)

	def setNome(self, nome):
		self.__nome = nome

	def getNome(self):
		return self.__nome

	def setSalario(self, salario):
		self.__salario = salario

	def getSalario(self):
		return self.__salario

	def setCpf(self, cpf):
		self.__cpf = cpf

	def getCpf(self):
		return self.__cpf

	def setEndereco(self, endereco):
		self.__endereco = endereco

	def getEndereco(self):
		return self.__endereco

	def setIdade(self, idade):
		self.__idade = idade

	def getIdade(self):
		return self.__idade

	def imprimir(self):
		print("Nome: " +  self.getNome())
		print("Salario: %5.2f" %self.getSalario())
		print("CPF: " +  self.getCpf())
		print("Endereco: " +  self.getEndereco())
		print("Idade: %d" %self.getIdade())