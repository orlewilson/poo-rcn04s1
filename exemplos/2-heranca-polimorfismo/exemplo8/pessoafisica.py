"""

Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		27/10/2016

Autor:		Orlewilson B. Maia
Descrição:	Classe que representará informações
			sobre uma pessoa física

"""

from pessoa import Pessoa

#Definindo Classe
class PessoaFisica(Pessoa):

	#atributos
	__cpf = ""
	__dataNascimento = ""
	
	# Construtor (inicializa os atributos)
	def __init__ (self, 
				  nome = "",
				  cpf = "",
				  dataNascimento = ""):
		super().__init__(nome)
		self.setCpf(cpf)
		self.setDataNascimento(dataNascimento)

	# Alterar conteúdo do atributo cpf
	def setCpf(self, cpf):
		self.__cpf = cpf			

	# Alterar conteúdo do atributo dataNascimento
	def setDataNascimento(self, dataNascimento):
		# obtém os valores
		dia = dataNascimento[0:2]
		mes = dataNascimento[3:5]
		ano = dataNascimento[6:10]

		if (dia.isnumeric() and mes.isnumeric() and ano.isnumeric()):
			self.__dataNascimento = dataNascimento	

	# Recuperar conteúdo do atributo cpf
	def getCpf(self):
		return self.__cpf


	# Recuperar conteúdo do atributo dataNascimento
	def getDataNascimento(self):
		return self.__dataNascimento

	
	# Imprimir informações sobre a pessoa física
	def imprimir(self):
		super().imprimir()
		
		print("Data Nascimento: " + self.getDataNascimento() + "\n")
		print("CPF: ", self.getCpf(), "\n")
		