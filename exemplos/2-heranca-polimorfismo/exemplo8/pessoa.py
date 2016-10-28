"""

Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		27/10/2016

Autor:		Orlewilson B. Maia
Descrição:	Classe que representará informações
			sobre uma pessoa

"""

#Definindo Classe
class Pessoa():

	#atributos
	__nome = ""
	
	# Construtor (inicializa os atributos)
	def __init__ (self, 
				  nome = ""):

		self.setNome(nome)

	# Alterar conteúdo do atributo nome
	def setNome(self, nome):
		if (not nome.isnumeric()):
			self.__nome = nome
	
	# Recuperar conteúdo do atributo nome
	def getNome(self):
		return self.__nome

	# Imprimir informações sobre a pessoa
	def imprimir(self):
		print("Nome: " + self.getNome() + "\n")
		