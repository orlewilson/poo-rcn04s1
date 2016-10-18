"""

Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		28/09/2016

Autor:		Orlewilson B. Maia
Descrição:	Classe que representará informações
			sobre um aluno herdando da classe pessoa

"""

# importando classe
from pessoa import Pessoa

#Definindo Classe com herança
class Aluno(Pessoa):

	#Definição dos atributos
	# __ torna o atributo não visível ao objeto
	__nomeCurso = ""
	__bolsista = False
	__periodo = 1

	# Construtor (inicializa os atributos)
	def __init__(self, 
				 nome = "",
				 endereco = "",
				 dataNascimento = "",
				 cpf = "",
				 matricula = "",
				 nomeCurso = "",
				 bolsista = "Não",
				 periodo = 1):
		# Primeira Forma
		#Pessoa.setNome(self, nome)
		#Pessoa.setEndereco(self, endereco)
		#Pessoa.setDataNascimento(self, dataNascimento)
		#Pessoa.setCpf(self, cpf)
		#Pessoa.setMatricula(self, matricula)
		
		# Segunda Forma
		#Pessoa.__init__(self, nome, endereco, 
		#	dataNascimento, cpf, matricula)

		# Terceira Forma
		super().__init__(nome, endereco, 
			dataNascimento, cpf, matricula)

		self.setNomeCurso(nomeCurso)
		self.setBolsista(bolsista)
		self.setPeriodo(periodo)

	# Definição dos métodos para manipular dados
	# (alterar e recuperar) de um atributo
	
	# Alterar conteúdo do atributo nomeCurso
	def setNomeCurso(self, nomeCurso):
		if (not nomeCurso.isnumeric()):
			self.__nomeCurso = nomeCurso	

	def setPeriodo(self, periodo):
		self.__periodo = periodo	

	# Alterar conteúdo do atributo bolsista
	def setBolsista(self, bolsista):
		
		if (bolsista.lower() == 'sim'):
		#if (bolsista.upper() == 'SIM'):
			self.__bolsista = True
		
		elif (bolsista.lower() == 'não'):
			self.__bolsista = False

	# Recuperar conteúdo do atributo periodo
	def getPeriodo(self):
		return self.__periodo

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

		# Primeira forma
		#print("Nome: " + Pessoa.getNome(self) + "\n")
		#print("Endereço: " + Pessoa.getEndereco(self) + "\n")
		#print("Data Nascimento: " + Pessoa.getDataNascimento(self) + "\n")
		#print("CPF: " + Pessoa.getCpf(self) + "\n")
		#print("Matricula: " + Pessoa.getMatricula(self) + "\n")
		
		# Segunda forma
		#Pessoa.imprimir(self)

		# Terceira forma
		super().imprimir()

		print("Nome Curso: ", self.getNomeCurso(), "\n")
		print("Bolsista: " + self.getBolsista() + "\n")
		print("Período: " + str(self.getPeriodo()) + "\n")
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
