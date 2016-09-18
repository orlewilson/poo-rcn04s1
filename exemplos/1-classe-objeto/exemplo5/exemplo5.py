"""
Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		14/09/2016

Autor:		Orlewilson B. Maia
Descrição:	Arquivo para testar a classe Aluno

"""
# importar arquivos
from aluno import Aluno

#Criando objeto a partir de uma classe
aluno1 = Aluno("Orlewilson")
aluno2 = Aluno()

#Atribuindo valores aos atributos do objeto aluno1
aluno1.setNome(input("Digite seu nome:"))
aluno1.setEndereco(input("Digite seu endereço:"))
aluno1.setDataNascimento(input("Digite sua data de nascimento:"))
aluno1.setNomeCurso(input("Digite seu curso: "))
aluno1.setBolsista(input("Você é bolsista?"))

# Imprimir conteúdos do objeto aluno1
#print("Nome: " + aluno1.getNome() + "\n")
#print("Endereço: " + aluno1.getEndereco() + "\n")
#print("Data Nascimento: " + aluno1.getDataNascimento() + "\n")
#print("Nome Curso: ", aluno1.getNomeCurso(), "\n")
#print("Bolsista: " + aluno1.getBolsista() + "\n")

aluno1.imprimir()