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
	
	# Recuperar conteúdo do atributo nome
	def getNome(self):
		return self.__nome


#Fim da classe Aluno -----------------------------



# Programa Principal

#Criando objeto a partir de uma classe
aluno1 = Aluno()

#Atribuindo valores aos atributos do objeto aluno1
aluno1.setNome(input("Digite seu nome:"))
#aluno1.endereco = input("Digite seu endereço:")
#aluno1.dataNascimento = input("Digite sua data de nascimento:")
#aluno1.nomeCurso = input("Digite seu curso: ")
#aluno1.bolsista = bool(input("Você é bolsista?"))

# Imprimir conteúdos do objeto aluno1
print("Nome: " + aluno1.getNome() + "\n")
#print("Endereço: " + aluno1.endereco + "\n")
#print("Data Nascimento: " + aluno1.dataNascimento + "\n")
#print("Nome Curso: ", aluno1.nomeCurso, "\n")
#print("Bolsista: " + str(aluno1.bolsista) + "\n")

"""
Tarefa para casa: 

1) Criar os demais métodos para garantir o encapsulamento dos 
   demais atributos.
2) Validar os valores de cada método get antes de atribuir os 
   valores aos seus respectivos atributos.
"""