"""
Disciplina:	Programação Orientada a Objetos
Professor:	Orlewilson B. Maia
Turma:		RCN04S1

Autor:		Orlewilson B. Maia
Data:		29/11/2016
Descrição:	Classe para representar dados de um 
		    Fibonacci

"""

class Fibonacci():


	def fib(self,n):

		if (n == 1 or n == 2):
			return 1
		else:
			return self.fib(n-2) + self.fib(n-1)

	def imprimirSequencia(self,n):
		for x in range (1, n):
			print (str(self.fib(x)) + " + ", end='')
		print ("")

teste = Fibonacci()
teste.imprimirSequencia(10)