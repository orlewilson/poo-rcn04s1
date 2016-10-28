"""
Disciplina:	Programação Orientada a Objetos
Turma:		RCN04S1
Professor:	Orlewilson Bentes Maia
Data:		29/10/2016

Autor:		Orlewilson B. Maia
Descrição:	Arquivo para testar as classes Pessoa, PessoaFisica e PessoaJuridica

"""

# importar arquivos
from pessoa import Pessoa
from pessoafisica import PessoaFisica
from pessoajuridica import PessoaJuridica

#Criando objeto a partir de uma classe
pessoa = Pessoa("maia")
pessoa.imprimir()

pessoaFisica = PessoaFisica("orlewilson", "1123", "05/10/1984")
pessoaFisica.imprimir()

pessoaJuridica = PessoaJuridica("orlewilson", "123141/0001-2", "1234", "Teste" , "Olá Mundo")
pessoaJuridica.imprimir()
