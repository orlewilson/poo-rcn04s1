"""

Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		28/09/2016

Autor:		Orlewilson B. Maia
Descrição:	Classe que representará informações
			sobre uma pessoa

"""

#Definindo Classe
class Pessoa():

	#atributos
	__nome = ""
	__endereco = ""
	__cpf = ""
	__dataNascimento = ""
	__matricula = ""

	# Construtor (inicializa os atributos)
	def __init__ (self, 
				  nome = "",
				  endereco = "",
				  cpf = "",
				  dataNascimento = "",
				  matricula = ""):

		self.setNome(nome)
		self.setEndereco(endereco)
		self.setCpf(cpf)
		self.setDataNascimento(dataNascimento)
		self.setMatricula(matricula)

	# Alterar conteúdo do atributo nome
	def setNome(self, nome):
		if (not nome.isnumeric()):
			self.__nome = nome
	
	# Alterar conteúdo do atributo endereco
	def setEndereco(self, endereco):
		if (not endereco.isnumeric()):
			self.__endereco = endereco	

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

	# Alterar conteúdo do atributo matricula
	def setMatricula(self, matricula):
		self.__matricula = matricula

	# Recuperar conteúdo do atributo nome
	def getNome(self):
		return self.__nome

	# Recuperar conteúdo do atributo endereco
	def getEndereco(self):
		return self.__endereco

	# Recuperar conteúdo do atributo cpf
	def getCpf(self):
		return self.__cpf


	# Recuperar conteúdo do atributo dataNascimento
	def getDataNascimento(self):
		return self.__dataNascimento

	# Recuperar conteúdo do atributo matricula
	def getMatricula(self):
		return self.__matricula


	# Imprimir informações sobre a pessoal
	def imprimir(self):
		print("Nome: " + self.getNome() + "\n")
		print("Endereço: " + self.getEndereco() + "\n")
		print("Data Nascimento: " + self.getDataNascimento() + "\n")
		print("CPF: ", self.getCpf(), "\n")
		print("Matricula: " + self.getMatricula() + "\n")