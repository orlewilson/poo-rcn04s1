"""

Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		27/10/2016

Autor:		Orlewilson B. Maia
Descrição:	Classe que representará informações
			sobre uma pessoa jurídica

"""

from pessoa import Pessoa

#Definindo Classe
class PessoaJuridica(Pessoa):

	#atributos
	__cnpj = ""
	__inscricaoEstadual = ""
	__nomeFantasia = ""
	__razaoSocial  = ""
	
	# Construtor (inicializa os atributos)
	def __init__ (self, 
				  nome = "",
				  cnpj = "",
				  inscricaoEstadual = "",
				  nomeFantasia = "",
				  razaoSocial  = ""):
		
		super().__init__(nome)
		self.setCnpj(cnpj)
		self.setInscricaoEstadual(inscricaoEstadual)
		self.setNomeFantasia(nomeFantasia)
		self.setRazaoSocial(razaoSocial)
		

	# Alterar conteúdo do atributo cnpj
	def setCnpj(self, cnpj):
		self.__cnpj = cnpj			

	# Alterar conteúdo do atributo inscricaoEstadual
	def setInscricaoEstadual(self, inscricaoEstadual):
		self.__inscricaoEstadual = inscricaoEstadual	

	# Alterar conteúdo do atributo nomeFantasia
	def setNomeFantasia(self, nomeFantasia):
		self.__nomeFantasia = nomeFantasia

	# Alterar conteúdo do atributo razaoSocial
	def setRazaoSocial(self, razaoSocial):
		self.__razaoSocial = razaoSocial

	# Recuperar conteúdo do atributo cnpj
	def getCnpj(self):
		return self.__cnpj

	# Recuperar conteúdo do atributo inscricaoEstadual
	def getInscricaoEstadual(self):
		return self.__inscricaoEstadual

	# Recuperar conteúdo do atributo nomeFantasia
	def getNomeFantasia(self):
		return self.__nomeFantasia

	# Recuperar conteúdo do atributo razaoSocial
	def getRazaoSocial(self):
		return self.__razaoSocial


	
	# Imprimir informações sobre a pessoa física
	def imprimir(self):
		super().imprimir()
		
		print("CNPJ: " + self.getCnpj() + "\n")
		print("Inscrição Estadual: ", self.getInscricaoEstadual(), "\n")
		print("Nome Fantasia: ", self.getNomeFantasia(), "\n")
		print("Razão Social: ", self.getRazaoSocial(), "\n")
		