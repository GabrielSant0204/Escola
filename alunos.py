from pessoa_fisica import PessoaFisica

class Aluno(PessoaFisica):
    def __init__(self, nome, cpf, rg, data_nascimento, cgm, turma, turno):
        super().__init__(nome,cpf, rg, data_nascimento)
        self.__cgm = cgm
        self.__turma = turma
        self.__turno = turno

    @property
    def cgm(self):
        return self.__cgm

    @property
    def turma(self):
        return self.__turma

    @property
    def turno(self):
        return self.__turno

    def acessarEscola(self, codigo_acesso):
        if codigo_acesso == self.cgm:
            print(f'Boa aula aluno(a), {super().nome}\n')
            return True
        else:
            return False






    def __str__(self):
        return f' Aluno:\n Nome: {super().nome}\n CPF:{super().cpf}\n RG:{super().rg}\n \
Data de nascimento:{super().data_nascimento}\n CGM:{self.cgm}\n\n'
