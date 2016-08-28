"""

Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		23/08/2016

Autor:		Orlewilson B. Maia
Descrição:	Exemplo de criação de classe em Python

"""

#Definindo Classe
class Aluno():

	#Definição dos atributos
	nome = ""
	endereco = ""
	dataNascimento = ""
	nomeCurso = ""
	bolsista = False

#Fim da classe Aluno -----------------------------


# Programa Principal

#Criando objeto a partir de uma classe
aluno1 = Aluno()

#Atribuindo valores aos atributos do objeto aluno1
aluno1.nome = "Orlewilson"
aluno1.endereco = "Rua São Paulo"
aluno1.dataNascimento = "05/05/1984"
aluno1.nomeCurso = "Tec. Redes de Computadores"
aluno1.bolsista = True

# Imprimir conteúdos do objeto aluno1
print("Nome: " + aluno1.nome + "\n")
print("Endereço: " + aluno1.endereco + "\n")
print("Data Nascimento: " + aluno1.dataNascimento + "\n")
print("Nome Curso: ", aluno1.nomeCurso, "\n")
print("Bolsista: " + str(aluno1.bolsista) + "\n")
