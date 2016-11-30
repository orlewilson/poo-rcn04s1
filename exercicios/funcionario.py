"""
Disciplina:	Programação Orientada a Objetos
Professor:	Orlewilson B. Maia
Turma:		RCN04S1

Autor:		Orlewilson B. Maia
Data:		29/11/2016
Descrição:	Classe para representar dados de um 
		    funcionario

"""

class Funcionario():

	# atributos
	__nome = ""
	__salario = 0.0
	
	# construtor
	def __init__(self, 
				 nome = "", 
				 salario = 0.0):
		self.setNome(nome)
		self.setSalario(salario)

	def setNome(self, nome):
		self.__nome = nome

	def getNome(self):
		return self.__nome

	def setSalario(self, salario):
		self.__salario = salario

	def getSalario(self):
		return self.__salario

	def aumentarSalario(self, valor):
		self.__salario = self.__salario + 
			self.__salario*valor/100
		
		#self.setSalario(self.getSalario() + 
		#	self.getSalario()*valor/100)

# Exemplo objeto
harry=Funcionario("Harry",25000)  
print("Salário Atual: ", harry.getSalario())
harry.aumentarSalario(15.7) 
print("Salário com Aumento: ", harry.getSalario())
