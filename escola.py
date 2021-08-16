from alunos import Aluno
from professor import Professor
from funcionario import Funcionario


class Escola():
    def __init__(self):
        self.__nome = "Escola de Programadores do Edutech"

        jose = Aluno('José', '333.666.444.89', '987.456.489-8', '19/08/2003', '12332115', '3A', 'tarde')
        pedro = Aluno('Pedro', '333.667.444.79', '187.436.489-8', '26/12/2003', '12367115', '3A', 'tarde')
        ana = Professor('Ana', '666.888.777.96', '555.888.444-3', '26/09/2000', 'Biologia', 'Formada')
        maria = Funcionario('Maria', '222.333.444-89', '111.888.269.8', '31/02/1999', 'R$1569,22', "Bibliotecária",
                            '13h30 às 16h30')

        self.__pessoas = [jose, pedro, ana, maria]

    def __getitem__(self, item):
        return self.__pessoas[item]

    def __len__(self):
        return len(self.__pessoas)

    def solicita_acesso(self):
        codigo_acesso = input('Código de acesso:   ')
        for p in self.__pessoas:
            if p.acessarEscola(codigo_acesso):
                return True
        print('Acesso negado')
        return False