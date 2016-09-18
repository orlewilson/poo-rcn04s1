"""

Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		14/09/2016

Autor:		Orlewilson B. Maia
Descrição:	Classe que representará informações
			sobre um aluno

"""

#Definindo Classe
class Aluno():

	#Definição dos atributos
	# __ torna o atributo não visível ao objeto
	__nome = ""
	__endereco = ""
	__dataNascimento = ""
	__nomeCurso = ""
	__bolsista = False

	# Construtor (inicializa os atributos)
	# Primeira forma
	"""
	def __init__(self):
		self.__nome = "Orlewilson"
		self.__endereco = "Rua São João"
		self.__dataNascimento = "05/05/1984"
		self.__nomeCurso = "Redes"
		self.__bolsista = True
	
	# Segunda forma
	def __init__(self, 
				 nome = "",
				 endereco = "",
				 dataNascimento = "",
				 nomeCurso = "",
				 bolsista = False):
		self.__nome = nome
		self.__endereco = endereco
		self.__dataNascimento = dataNascimento
		self.__nomeCurso = nomeCurso
		self.__bolsista = bolsista
	"""
	# Terceira forma
	def __init__(self, 
				 nome = "",
				 endereco = "",
				 dataNascimento = "",
				 nomeCurso = "",
				 bolsista = "Não"):
		self.setNome(nome)
		self.setEndereco(endereco)
		self.setDataNascimento(dataNascimento)
		self.setNomeCurso(nomeCurso)
		self.setBolsista(bolsista)

	# Definição dos métodos para manipular dados
	# (alterar e recuperar) de um atributo
	
	# Alterar conteúdo do atributo nome
	def setNome(self, nome):
		
		# isnumeric() verifica se é um valor totalmente numérico.
		# Se verdadeiro, retorna True. Caso contrário, retorna False.
		# Para mais informações: 
		# https://docs.python.org/3/library/stdtypes.html?highlight=isnumeric#str.isnumeric
		if (not nome.isnumeric()):
			self.__nome = nome
	
	# Alterar conteúdo do atributo endereco
	def setEndereco(self, endereco):
		if (not endereco.isnumeric()):
			self.__endereco = endereco	

	# Alterar conteúdo do atributo dataNascimento
	def setDataNascimento(self, dataNascimento):
		# obtém os valores
		dia = dataNascimento[0:2]
		mes = dataNascimento[3:5]
		ano = dataNascimento[6:10]

		if (dia.isnumeric() and mes.isnumeric() and ano.isnumeric()):
			self.__dataNascimento = dataNascimento	

	# Alterar conteúdo do atributo nomeCurso
	def setNomeCurso(self, nomeCurso):
		if (not nomeCurso.isnumeric()):
			self.__nomeCurso = nomeCurso	

	# Alterar conteúdo do atributo bolsista
	def setBolsista(self, bolsista):
		
		if (bolsista.lower() == 'sim'):
		#if (bolsista.upper() == 'SIM'):
			self.__bolsista = True
		
		elif (bolsista.lower() == 'não'):
			self.__bolsista = False

	# Recuperar conteúdo do atributo nome
	def getNome(self):
		return self.__nome

	# Recuperar conteúdo do atributo endereco
	def getEndereco(self):
		return self.__endereco

	# Recuperar conteúdo do atributo dataNascimento
	def getDataNascimento(self):
		return self.__dataNascimento

	# Recuperar conteúdo do atributo nomeCurso
	def getNomeCurso(self):
		return self.__nomeCurso

	# Recuperar conteúdo do atributo bolsista
	def getBolsista(self):
		if (self.__bolsista):
			return "Sim"
		else:
			return "Não"

	# Imprimir informações sobre o aluno
	def imprimir(self):
		print("Nome: " + self.getNome() + "\n")
		print("Endereço: " + self.getEndereco() + "\n")
		print("Data Nascimento: " + self.getDataNascimento() + "\n")
		print("Nome Curso: ", self.getNomeCurso(), "\n")
		print("Bolsista: " + self.getBolsista() + "\n")
		print("Mensalidade: " + str(self.mensalidadeCurso()) + "\n")

	def mensalidadeCurso(self):
		if (self.getNomeCurso().lower() == "redes"):
			return 800.00
		elif (self.getNomeCurso().lower() == "ciência"):
			return 1100.00
		elif (self.getNomeCurso().lower() == "engenharia"):
			return 1300.00
		else:
			return 0.0


#Fim da classe Aluno -----------------------------
