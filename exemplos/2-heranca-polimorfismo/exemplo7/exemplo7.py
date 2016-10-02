"""
Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		29/09/2016

Autor:		Orlewilson B. Maia
Descrição:	Arquivo para testar as classes Aluno e Professor

"""

# importar arquivos
from aluno import Aluno
from professor import Professor

#Criando objeto a partir de uma classe
aluno1 = Aluno("Orlewilson")
aluno1.imprimir()

prof1 = Professor("José")
prof1.setSalario(2000)
prof1.imprimir()