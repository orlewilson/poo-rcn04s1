"""

Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		28/09/2016

Autor:		Orlewilson B. Maia
Descrição:	Classe que representará informações
			sobre um professor herdando da classe pessoa

"""

# importando classe
from pessoa import Pessoa

#Definindo Classe com herança

class Professor(Pessoa):

	# atributos
	__salario = 0.0
	__disciplinas = ""

	# construtor
	def __init__(self, 
				 nome = "",
				 endereco = "",
				 dataNascimento = "",
				 cpf = "",
				 matricula = "",
				 salario = 0.0,
				 disciplinas = ""):
		# Primeira Forma
		Pessoa.setNome(self, nome)
		Pessoa.setEndereco(self, endereco)
		Pessoa.setDataNascimento(self, dataNascimento)
		Pessoa.setCpf(self, cpf)
		Pessoa.setMatricula(self, matricula)
		
		self.setDisciplinas(disciplinas)
		self.setSalario(salario)
	
	# Alterar conteúdo do atributo disciplinas
	def setDisciplinas(self, disciplinas):
		if (not disciplinas.isnumeric()):
			self.__disciplinas = disciplinas

	# Alterar conteúdo do atributo salario
	def setSalario(self, salario):
		self.__salario = salario

	# Recuperar conteúdo do atributo disciplinas
	def getDisciplinas(self):
		return self.__disciplinas

	# Recuperar conteúdo do atributo salário
	def getSalario(self):
		return self.__salario


	# Imprimir informações sobre o aluno
	def imprimir(self):
		print("Nome: " + Pessoa.getNome(self) + "\n")
		print("Endereço: " + Pessoa.getEndereco(self) + "\n")
		print("Data Nascimento: " + Pessoa.getDataNascimento(self) + "\n")
		print("CPF: " + Pessoa.getCpf(self) + "\n")
		print("Matricula: " + Pessoa.getMatricula(self) + "\n")
		
		print("Salario: %5.2f\n" %(self.getSalario()))
		print("Disciplinas: " + self.getDisciplinas() + "\n")
		