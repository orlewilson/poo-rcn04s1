"""
Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		21/09/2016

Autor:		Orlewilson B. Maia
Descrição:	Arquivo para testar a classe Professor

"""

# importar arquivos
from professor import Professor

#Criando objeto a partir de uma classe
prof1 = Professor()
prof1 = Professor("Elias")
prof1 = Professor("Elias",6900)
prof1 = Professor("Elias",6900, "123")
prof1 = Professor("Elias",6900, "123", "Rua j")
prof1 = Professor("Elias",6900, "123", "Rua j", 80)

prof2 = Professor("Audilene", 15000, "345", "Rua k", 75)
prof3 = Professor("Camilo", 2, "345", "Rua m", 110)
prof4 = Professor("Alberto", 3.5, "456", "Rua g", 30)
prof5 = Professor("Orlewilson", 910, "345", "Rua g", 15)

prof1.imprimir()