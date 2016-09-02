"""

Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		26/08/2016

Autor:		Orlewilson B. Maia
Descrição:	Exemplo de encapsulamento

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

#Fim da classe Aluno -----------------------------



# Programa Principal

#Criando objeto a partir de uma classe
aluno1 = Aluno()

#Atribuindo valores aos atributos do objeto aluno1
aluno1.setNome(input("Digite seu nome:"))
aluno1.setEndereco(input("Digite seu endereço:"))
aluno1.setDataNascimento(input("Digite sua data de nascimento:"))
aluno1.setNomeCurso(input("Digite seu curso: "))
aluno1.setBolsista(input("Você é bolsista?"))

# Imprimir conteúdos do objeto aluno1
print("Nome: " + aluno1.getNome() + "\n")
print("Endereço: " + aluno1.getEndereco() + "\n")
print("Data Nascimento: " + aluno1.getDataNascimento() + "\n")
print("Nome Curso: ", aluno1.getNomeCurso(), "\n")
print("Bolsista: " + aluno1.getBolsista() + "\n")

"""
Tarefa para casa: 

1) Criar os demais métodos para garantir o encapsulamento dos 
   demais atributos.
2) Validar os valores de cada método get antes de atribuir os 
   valores aos seus respectivos atributos.
"""